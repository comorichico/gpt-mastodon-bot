# gpt-mastodon-bot
GPT-3のAPIを利用したmastodon向けのおしゃべり人工知能BOTです。

使い方：
Pythonのインストールをしてない人はPythonをインストールしてください。
WindowsPCであればMicrosoftStoreでPythonと検索してインストールするのが楽です。
動作確認はPython3.10で行っています。

まず最初にコマンドプロンプト、powershell、ターミナルなどから
pip install mastodon.py
pip install openai
を実行します。

mastodonにBOT用のアカウントを作ってください。

setup.pyの中身を書き換えます。
mastodon_url、mastodon_login_mail、mastodon_login_passwordを自分の環境で使えるものに書き換えます。
cred_file_nameはそのままでいいでしょう。
app_nameは好きなものに変えても良いです。

python setup.py
で実行するとログインに使うファイルが生成されます。

その後
python gpt.py
で実行するとBOTが起動します。

あとはBOTにメンションをつけて話しかけてみましょう。
返事があれば成功です。
おしゃべりを楽しみましょう！
