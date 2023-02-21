from mastodon import Mastodon, StreamListener
import sqlite3
from contextlib import closing
import openai
import os
from dotenv import load_dotenv

# 1日の上限の文字数
str_limit = 500

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]

# データベース名
dbname = "gpt.db"

class Stream(StreamListener):
    def __init__(self):
        super(Stream, self).__init__()

    def on_notification(self,notif): #通知が来た時に呼び出されます
        if notif['type'] == 'mention': #通知の内容がリプライかチェック
            content = notif['status']['content'] #リプライの本体です
            id = notif['status']['account']['username']
            st = notif['status']
            main(content, st, id)

def main(content,st,id):
    global DBFlag
    global keywordMemory
    global dbname
    global keywordAuthor
    req = content.rsplit(">")[-2].split("<")[0].strip()

    str_count = -1
    limit = -1

    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()
        create_table = "CREATE TABLE IF NOT EXISTS users(userid, str_count, str_limit, PRIMARY KEY(userid))"
        c.execute(create_table)
        sql = "select str_count, str_limit from users where userid = ?"
        word = (id,)
        result = c.execute(sql, word)
        for row in result:
            if row[0] != "":
                str_count = row[0]
                limit = row[1]

        if str_count != -1:
            # 1日に会話できる上限を超えていた場合
            # メッセージを表示して処理を終わる
            if len(req) + str_count > limit:
                reply_text = "お話できる1日の上限を超えました。"
                reply_text += "日本時間の0時を過ぎるとリセットされるので"
                reply_text += "また明日試してみてください。"
                reply_text += "今日はいっぱい話しかけてくれてありがとう！"

                mastodon.status_reply(st,
                        reply_text,
                        id,
                        visibility='public')
                return

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=req,
        temperature=1.0,
        top_p=0.9,
        max_tokens=512,
        stop=["<|endoftext|>"],
    )
    reply = response.choices[0].text.strip()
    mastodon.status_reply(st,
            reply,
            id,
            visibility='public')

    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()
        sql = "INSERT OR REPLACE INTO users (userid, str_count, str_limit) values (?,?,?)"
        if str_count == -1:
            str_count = 0
            limit = str_limit

        str_count = str_count + len(req)
        words = (id , str_count, limit)
        c.execute(sql, words)
        conn.commit()

mastodon = Mastodon(access_token = 'gptchan_clientcred.txt')

print("起動しました")
mastodon.stream_user(Stream()) #ストリームの起動