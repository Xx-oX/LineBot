import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, PostbackEvent, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()


machine = TocMachine(
    states=["user", "intro", "fsm", "menu", "write", "read", "change", "write_content", "read_show", "change_select", "change_content"],
    transitions=[
        {
            "trigger": "advance",
            "source": ["menu", "user"],
            "dest": "intro",
            "conditions": "is_going_to_intro",
        },
        {
            "trigger": "advance",
            "source": ["menu", "user"],
            "dest": "fsm",
            "conditions": "is_going_to_fsm",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "menu",
            "conditions": "is_going_to_menu",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "write",
            "conditions": "is_going_to_write",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "read",
            "conditions": "is_going_to_read",
        },
        {
            "trigger": "advance",
            "source": "menu",
            "dest": "change",
            "conditions": "is_going_to_change",
        },
        {
            "trigger": "advance",
            "source": "write",
            "dest": "write_content",
            "conditions": "is_going_to_write_content",
        },
        {
            "trigger": "advance",
            "source": "read",
            "dest": "read_show",
            "conditions": "is_going_to_read_show",
        },
        {
            "trigger": "advance",
            "source": "read_show",
            "dest": "read",
            "conditions": "is_going_back_to_read",
        },
        {
            "trigger": "advance",
            "source": "change",
            "dest": "change_select",
            "conditions": "is_going_to_change_select",
        },
        {
            "trigger": "advance",
            "source": "change_select",
            "dest": "change_content",
            "conditions": "is_going_to_change_content",
        },
        {
            "trigger": "advance",
            "source": ["menu", "write", "read", "change", "write_content", "read_show", "change_select", "change_content"],
            "dest": "menu",
            "conditions": "is_going_back_to_menu",
        },
        {"trigger": "go_back", "source": ["intro", "fsm", "menu"], "dest": "user"}
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if isinstance(event, PostbackEvent):
            pass
        elif isinstance(event, MessageEvent):
            if not isinstance(event.message, TextMessage):
                continue
            if not isinstance(event.message.text, str):
                continue
        else:
            continue
        
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            listState = ["write", "read", "change", "write_content", "read_show", "change_select", "change_content"]
            if machine.state in listState:
                send_text_message(event.reply_token, "Type \"back\" to go back ><")
            else:
                send_text_message(event.reply_token, "Not Entering any State")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ['PORT']
    app.run(host="0.0.0.0", port=port, debug=False)