from transitions.extensions import GraphMachine

from utils import send_text_message, send_flex_message
from layout import flex_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    # edges

    def is_going_to_intro(self, event):
        text = event.message.text
        return text.lower() == "introduction"

    def is_going_to_fsm(self, event):
        text = event.message.text
        return text.lower() == "fsm"

    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "start"

    def is_going_to_write(self, event):
        text = event.message.text
        return text.lower() == "write"

    def is_going_to_read(self, event):
        text = event.message.text
        return text.lower() == "read"

    def is_going_to_change(self, event):
        text = event.message.text
        return text.lower() == "change"

    def go_back_to_menu(self, event):
        text = event.message.text
        return text.lower() == "menu"

    # vertices

    def on_enter_intro(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "Introduction")
        self.go_back()

    def on_exit_intro(self):
        print("Leaving intro...")

    def on_enter_fsm(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "FSM")
        self.go_back()

    def on_exit_fsm(self):
        print("Leaving fsm...")

    def on_enter_menu(self, event):
        reply_token = event.reply_token
        # send_text_message(reply_token, "Opening the diary...")
        flex_msg = flex_message
        send_flex_message(reply_token, "Choose what you want to do", flex_msg)

    def on_exit_menu(self, event):
        print("Leaving menu...")

    def on_enter_write(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "write")

    def on_exit_write(self, event):
        print("Leaving write...")

    def on_enter_read(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "read")

    def on_exit_read(self, event):
        print("Leaving read...")

    def on_enter_change(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "change")

    def on_exit_change(self, event):
        print("Leaving change...")
