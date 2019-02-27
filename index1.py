from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "<h1>Привет, Яндекс!</h1>"


@app.route('/image_sample')
def image():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width,
                    initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                    crossorigin="anonymous">
                    <title>Это Риана</title>
                  </head>
                  <body>
                    <div class="alert alert-primary" role="alert">
                        <img src="{}" alt="это сова">
                    </div>
                   </body>
                </html>'''.format(url_for('static', filename='img/bird.jpeg'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
