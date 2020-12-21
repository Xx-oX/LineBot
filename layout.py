flex_msg_intro = {
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "image",
            "url": "https://live.staticflickr.com/11/15846725_080106f0c1_k.jpg",
            "size": "full",
            "aspectMode": "cover",
            "aspectRatio": "120:80",
            "gravity": "center",
            "flex": 1
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "text",
                "text": "Xx-oX",
                "size": "xs",
                "color": "#ffffff",
                "align": "center",
                "gravity": "center"
              }
            ],
            "backgroundColor": "#EC3D44",
            "paddingAll": "2px",
            "paddingStart": "4px",
            "paddingEnd": "4px",
            "flex": 0,
            "position": "absolute",
            "offsetStart": "18px",
            "offsetTop": "18px",
            "cornerRadius": "100px",
            "width": "48px",
            "height": "25px"
          }
        ]
      }
    ],
    "paddingAll": "0px"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "contents": [],
                "size": "xl",
                "text": "Line Diary",
                "color": "#ffffff",
                "weight": "bold"
              },
              {
                "type": "text",
                "text": "2020-TOC-final project",
                "color": "#ffffffcc",
                "size": "sm"
              }
            ],
            "spacing": "sm"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "contents": [],
                    "size": "sm",
                    "margin": "lg",
                    "color": "#ffffffde",
                    "text": "You can keep your own diary here~\nSay \"hi\" to start : )"
                  }
                ],
                "paddingBottom": "xl"
              }
            ],
            "paddingAll": "13px",
            "backgroundColor": "#ffffff1A"
          }
        ]
      }
    ],
    "paddingAll": "20px",
    "backgroundColor": "#e0b646"
  }
}

flex_msg_menu = {
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
      },
      {
        "type": "text",
        "text": "Type \"back\" to return to this menu!!",
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

flex_msg_datepicker = {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "Select Date",
        "margin": "none",
        "align": "center"
      }
    ],
    "action": {
      "type": "datetimepicker",
      "label": "Select Time",
      "data": "returnData",
      "mode": "date",
      "max": "2999-12-31",
      "min": "1900-01-01",
      "initial": "2020-01-01"
    }
  }
}