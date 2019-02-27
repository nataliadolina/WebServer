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


@app.route('/bootstrap_sample')
def sample():
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
                       <title>Bootstrap – знакомство</title>
                     </head>
                     <body>
                       <nav class="navbar navbar-expand-lg navbar-light bg-light">
                          <a class="navbar-brand" href="#">Это</a>
                          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                            <span class="navbar-toggler-icon"></span>
                          </button>
                          <div class="collapse navbar-collapse" id="navbarNav">
                            <ul class="navbar-nav">
                              <li class="nav-item active">
                                <a class="nav-link" href="#">задача<span class="sr-only">(current)</span></a>
                              </li>
                              <li class="nav-item">
                                <a class="nav-link" href="#">из</a>
                              </li>
                              <li class="nav-item">
                                <a class="nav-link" href="#">яндекс</a>
                              </li>
                              <li class="nav-item">
                                <a class="nav-link disabled" href="#">лицея</a>
                              </li>
                            </ul>
                          </div>
                          <div id="carouselExampleSlidesOnly" class="carousel slide" data-ride="carousel">
                              <div class="carousel-inner">
                                <div class="carousel-item active">
                                  <img class="d-block w-100" src="{}" alt="First slide">
                                </div>
                                <div class="carousel-item">
                                  <img class="d-block w-100" src="{}" alt="Second slide">
                                </div>
                                <div class="carousel-item">
                                  <img class="d-block w-100" src="{}" alt="Third slide">
                                </div>
                              </div>
                            </div>
                        </nav>
                    </html>'''.format(url_for('static', filename='img/bird.jpeg'),
                                      url_for('static', filename='img/fox.jpg'), url_for('static',
                                                                                         filename='https://sweetpanda.ru/wp-content/uploads/2016/10/gettyimages-73726710.jpg'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
