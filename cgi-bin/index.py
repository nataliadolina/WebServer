from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс! Я - Наташа"


@app.route('/image_sample')
def image():
    return '''<img src="{}" alt="это сова">'''.format(url_for('static', filename='img/Риана.png'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
