from flask import Flask, request, abort, send_from_directory
import csv
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,ImageMessage,ImageSendMessage
)
from linebot.models.responses import Content
from werkzeug.datastructures import ContentSecurityPolicy
from werkzeug.wrappers import response

app = Flask(__name__)

line_bot_api = LineBotApi('NOeaOOsqqgUAsniYooBMkvTJHb1ny7FvpeuLFrszjK5PxKAKu+r6uZkPfRYB7ThIbxBX0aXiKnpWMi1bWNLBQ1eLESPlXb21KFRixA6V302K1w5iZt7aJd/lp/Le6JIyoPVvelBhWB14smzkR7Oh/gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('64a096a350094555299d79a1560663c1')

@app.route("/")
def test():
    return "OK"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'
def ann():
    count = 0  # count変数をここで初期化する
    s=[]
    i = []
    x=""
    n=""
    m=""
    with open('infreezer.csv', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if count == 2:  # 3番目の行をチェック (0ベースのインデックス)
                i.append(row)
                x+=str(i)
                x=x.strip('[\']')
            count += 1
        l = x.split()
        for i in l:
            n+=i
        s.append("れいぞうこの中身\n")
        s.append("--------------\n")
        for i in l:
            s.append(i)
            s.append("\n")
        for i in s:
            m+=i
    return m

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text=="@start":
        google_drive_url="https://drive.google.com/uc?id=16MMdtGnrgwlXq6OYjBVqMogcGNwcFagr"
        url = google_drive_url.replace("https://drive.google.com/file/d/", "https://drive.google.com/uc?id=").replace("/view?usp=sharing", "")
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url=google_drive_url,
                preview_image_url=google_drive_url))
    else:
        message=ann()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=message))



if __name__ == "__main__":
    app.run()