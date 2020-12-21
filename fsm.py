from transitions.extensions import GraphMachine
from linebot.models import PostbackEvent
from datetime import date

from utils import send_text_message, send_flex_message, send_date_picker, send_image_url
from layout import flex_msg_intro, flex_msg_menu, flex_msg_datepicker, img_fsm
from database import Database


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
        self.param_date=""

    # edges

    def is_going_to_intro(self, event):
        text = event.message.text
        return text.lower() == "?"

    def is_going_to_fsm(self, event):
        text = event.message.text
        return text.lower() == "fsm"

    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "hi"

    def is_going_to_write(self, event):
        text = event.message.text
        return text.lower() == "write"

    def is_going_to_read(self, event):
        text = event.message.text
        return text.lower() == "read"

    def is_going_to_change(self, event):
        text = event.message.text
        return text.lower() == "change"

    def is_going_to_write_content(self, event):
        return True

    def is_going_to_read_show(self, event):
        return True

    def is_going_back_to_read(self, event):
        text = event.message.text
        return text.lower() != "back"

    def is_going_to_change_select(self, event):
        return True

    def is_going_to_change_content(self, event):
        return True

    def is_going_back_to_menu(self, event):
        text = event.message.text
        return text.lower() == "back"

    # vertices

    def on_enter_intro(self, event):
        reply_token = event.reply_token
        flex_msg = flex_msg_intro
        send_flex_message(reply_token, flex_msg)
        self.go_back()

    def on_exit_intro(self):
        print("Leaving intro...")

    def on_enter_fsm(self, event):
        reply_token = event.reply_token
        send_image_url(reply_token, "https://imgur.com/Yhf65gd.png")
        self.go_back()

    def on_exit_fsm(self):
        print("Leaving fsm...")

    def on_enter_menu(self, event):
        reply_token = event.reply_token
        flex_msg = flex_msg_menu
        send_flex_message(reply_token, flex_msg)

    def on_exit_menu(self, event):
        print("Leaving menu...")

    def on_enter_write(self, event):
        d = date.today()
        reply_token = event.reply_token
        send_text_message(reply_token, str(d) + " :")

    def on_enter_write_content(self, event):
        d = date.today()
        c = event.message.text
        try:
            with Database() as db:
                if(db.getSize(d) == 0):
                    db.insert((None, d, c))
                    reply =  "saved~"
                else:
                    reply =  "Already written today : ( \nUse change~"
        finally:
            reply_token = event.reply_token
            send_text_message(reply_token, reply)

    def on_enter_read(self, event):
        reply_token = event.reply_token
        dp = flex_msg_datepicker
        send_date_picker(reply_token, dp)

    def on_enter_read_show(self, event):
        if not isinstance(event, PostbackEvent):
            self.go_back()
            return
        d = event.postback.params["date"]
        print(d)
        reply = "Nothing happended on this day : ("
        try:
            with Database() as db:
                content = db.read(d)
                if len(content) == 0:
                    reply = "Nothing happended on this day : ("
                else:
                    reply = content[0][2]
        finally:
            reply_token = event.reply_token
            send_text_message(reply_token, reply)

    def on_enter_change(self, event):
        reply_token = event.reply_token
        dp = flex_msg_datepicker
        send_date_picker(reply_token, dp)

    def on_enter_change_select(self, event):
        if not isinstance(event, PostbackEvent):
            self.go_back()
            return
        reply_token = event.reply_token
        d = event.postback.params["date"]
        print(d)
        self.param_date = d
        send_text_message(reply_token, str(d) + " :")

    def on_enter_change_content(self, event):
        d = self.param_date
        c = event.message.text
        try:
            with Database() as db:
                if(db.getSize(d) == 0):
                    db.insert((None, d, c))
                else:
                    db.update(d, c)
        finally:
            reply_token = event.reply_token
            send_text_message(reply_token, "Change saved : )")