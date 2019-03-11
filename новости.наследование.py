import json

from flask import Flask, request, url_for, render_template

app = Flask(__name__)


@app.route('/news', methods=['POST', 'GET'])
def news():
    with open("json_files/news", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    return render_template('news.html', news=news_list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
