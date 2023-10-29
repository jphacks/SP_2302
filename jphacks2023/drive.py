from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

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
