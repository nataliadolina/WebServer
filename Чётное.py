from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/odd_even', methods=['POST', 'GET'])
def odd_even():
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
                            crossorigin="anonymous"
                          </head>
                          <body>
                              <form method="post">
                                 <div class="form-group">
                                    <input type="number" class="form-control" id="number" placeholder="Введите число" name="number">
                                 </div>
                                 <div class="form-group">
                                     <button type="submit" class="btn btn-primary">готово</button>
                                 </div>
                              <form>
                          <body>'''
    elif request.method == 'POST':
        n = request.form['number']
        if not n.isdigit():
            n = False
        else:
            n = int(n)
        return render_template('odd_even', number=n)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
