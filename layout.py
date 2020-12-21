flex_message = {
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://live.staticflickr.com/3930/15232774180_217e303f95_k.jpg",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "md",
    "action": {
      "type": "uri",
      "uri": "https://github.com/Xx-oX/LineBot"
    },
    "contents": [
      {
        "type": "text",
        "text": "Line Diray",
        "size": "xl",
        "weight": "bold"
      },
      {
        "type": "text",
        "text": "Keep your own diary on \"Line\"!!",
        "color": "#aaaaaa",
        "size": "xxs"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "spacer",
        "size": "xxl"
      },
      {
        "type": "button",
        "style": "primary",
        "color": "#905c44",
        "action": {
          "type": "message",
          "label": "Write Diary!",
          "text": "write"
        }
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "spacer",
            "size": "xxl"
          },
          {
            "type": "button",
            "style": "primary",
            "color": "#905c44",
            "action": {
              "type": "message",
              "label": "Read Diary!",
              "text": "read"
            }
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "spacer",
            "size": "xxl"
          },
          {
            "type": "button",
            "style": "primary",
            "color": "#905c44",
            "action": {
              "type": "message",
              "label": "Change History!",
              "text": "change"
            }
          }
        ]
      }
    ]
  }
}

