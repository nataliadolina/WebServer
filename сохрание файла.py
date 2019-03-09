from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/file_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return '''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport"
                            content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                            integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                            crossorigin="anonymous">
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <form method="post" enctype="multipart/form-data">
                              <div class="form-group">
                                <label for="photo">Приложите фотографию</label>
                                <input type="file" class="form-control-file" id="photo" name="file">
                              </div>
                              <button type="submit" class="btn btn-primary">Отправить</button>
                            <form>
                          <body>'''
    elif request.method == 'POST':
        f = request.files['file']
        f.save()
        return 'форма отправлена'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
