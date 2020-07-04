import os
# splite3をimportする
import sqlite3
import math
# flaskをimportしてflaskを使えるようにする
from flask import Flask , render_template , request , redirect , session

from datetime import datetime
from tkinter import messagebox


# appにFlaskを定義して使えるようにしています。Flask クラスのインスタンスを作って、 app という変数に代入しています。
app = Flask(__name__)

# Flask では標準で Flask.secret_key を設定すると、sessionを使うことができます。この時、Flask では session の内容を署名付きで Cookie に保存します。
app.secret_key = 'sunabakoza'

# @app.route('/', methods=["GET", "POST"])
# def index():
#     conn = sqlite3.connect('niseco.db')
#     c = conn.cursor()
#     c.execute("select id,name from syouhin")
#     comment_list = []
#     for row in c.fetchall():
#         comment_list.append({"id": row[0],"name": row[1]})

#     c.close()
#     return render_template('index.html', comment_list = comment_list)

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(403)
def mistake403(code):
    return 'There is a mistake in your url!'


@app.errorhandler(404)
def notfound404(code):
    return "404だよ！！見つからないよ！！！"


# __name__ というのは、自動的に定義される変数で、現在のファイル(モジュール)名が入ります。 ファイルをスクリプトとして直接実行した場合、 __name__ は __main__ になります。
if __name__ == "__main__":
    # Flask が持っている開発用サーバーを、実行します。
    app.run()