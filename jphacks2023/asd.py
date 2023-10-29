from pydrive2.auth import GoogleAuth

gauth = GoogleAuth()
gauth.LocalWebserverAuth()  # ユーザーが認証するためのローカルウェブサーバーを起動し、認証を待ちます。認証情報を作成して保存します。

# 認証情報を将来の再実行で再利用するためにファイルに保存することもできます
gauth.SaveCredentialsFile("mycreds.txt")
