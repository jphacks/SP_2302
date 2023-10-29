from flask import Flask, request, abort, send_from_directory
import csv
from collections import Counter
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
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
import time



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
def ann(): #from collections import Counterも入れました
    count = 0  # count変数をここで初期化する
    s=[]
    i = []
    x=""
    n=""
    m=""
    with open('C:/Users/nanam/Desktop/workspaces/jphacks2023/runs/result/infreezer.csv', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if count == 2:  # 3番目の行をチェック (0ベースのインデックス)
                i.append(row)
                x+=str(i)
                x=x.strip('[\']')
            count += 1
        l = x.split()
        element_counts = Counter(l)
        s.append("れいぞうこの中身\n")
        s.append("--------------\n")
        for element,counts in element_counts.items():
            s.append(f"{element}: {counts}個\n")
        for i in s:
            m+=i
    return m

def ann2():
    count = 0  # count変数をここで初期化する
    s=[]
    i = []
    x=""
    n=""
    m=""
    with open('C:/Users/nanam/Desktop/workspaces/jphacks2023/runs/result/result.csv', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            if count == 0:  # 3番目の行をチェック (0ベースのインデックス)
                i.append(row)
                x+=str(i)
                x=x.strip('[\']')
            count += 1
        s.append("おすすめのレシピ:" +x)
        for i in s:
            m+=i
    return x


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text=="写真":
        gauth = GoogleAuth()

        # 保存した認証情報を読み込みます（利用可能な場合）
        gauth.LoadCredentialsFile("mycreds.txt")

        if gauth.credentials is None:
            # 存在しない場合、認証を試行します
            gauth.LocalWebserverAuth()

            # 次回の実行のために認証情報を保存します
            gauth.SaveCredentialsFile("mycreds.txt")

        drive = GoogleDrive(gauth)

        data_path = r"C:/Users/nanam/Desktop/workspaces/jphacks2023/runs/detect/predict/image0.jpg"

        f = drive.CreateFile(
            {
                'id': '1NUwT1nJSCWai8ngn9p83jqAYLCRDi6G0'
                # 'title': 'data_invest.jpg'
            }
        )
        f.SetContentFile(data_path)
        f.Upload()
        google_drive_url="https://drive.google.com/uc?id=1NUwT1nJSCWai8ngn9p83jqAYLCRDi6G0"
        url = google_drive_url.replace("https://drive.google.com/file/d/", "https://drive.google.com/uc?id=").replace("/view?usp=sharing", "")
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(
                original_content_url=google_drive_url,
                preview_image_url=google_drive_url))
    elif event.message.text=="スキャン":
        import cliant
        time.sleep(10)
        import test
        time.sleep(20)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage("スキャン完了"))
    elif event.message.text=="在庫":
        message=ann()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=message))
    elif event.message.text=="おすすめ料理":
        message=ann2()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=message))
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage("ご利用ありがとうございます。"))



if __name__ == "__main__":
    app.run()
