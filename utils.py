import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage, ImageSendMessage


channel_access_token = "ge4ebr1e5XBnqmlFogeV8grB8JzZTXhslMcZ6sDqzr/TxTmurm8YKfGsIa+Lt4tXXro0LIvzoRuzv1PU3VwTq7nSipl2zn0LL6aJYI92qu81YP4I1u+5E2GbG4bLnGp1Ee7xhMKrEkLDZVm6i1alagdB04t89/1O/w1cDnyilFU="
# channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_flex_message(reply_token, flex_msg):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, FlexSendMessage("menu", flex_msg))

    return "OK"

def send_date_picker(reply_token, datepicker):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, FlexSendMessage("data_picker", datepicker))

    return "OK"

def send_image_url(reply_token, img_url):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
    return "OK"

"""
def send_button_message(id, text, buttons):
    pass
"""
