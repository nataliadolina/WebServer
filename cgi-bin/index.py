from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс! Я - Наташа"


@app.route('/image_sample')
def image():
    return '''<img src="{}" alt="это сова">'''.format(url_for('static', filename='img/Риана.png'))


@app.route('/bootstrap_sample')
def sample():
    return '''<nav class="navbar navbar-toggleable-md navbar-light bg-faded">
    <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse">
    <div id="carousel-example-generic" class="carousel slide" data-ride="carousel">
    <div class="carousel-item active">
      <img src="{}" alt="First slide">
    </div>
    <div class="carousel-item">
      <img src="{}" alt="Second slide">>
    </div>
    <div class="carousel-item">
      <img src="http://127.0.0.1:8080/static/img/fox.jpg" alt="Third slide">
    </div>
  </div>'''.format(url_for('static', filename='img/Риана.png'), url_for('static', filename='img/Попугай.png'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
