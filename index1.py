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
                       <nav class="navbar navbar-toggleable-md navbar-light bg-faded">
                          <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                            <span class="navbar-toggler-icon"></span>
                          </button>
                          <a class="navbar-brand" href="#">Navbar</a>
                          <div class="collapse navbar-collapse" id="navbarNavDropdown">
                            <ul class="navbar-nav">
                              <li class="nav-item active">
                                <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
                              </li>
                              <li class="nav-item">
                                <a class="nav-link" href="#">Features</a>
                              </li>
                              <li class="nav-item">
                                <a class="nav-link" href="#">Pricing</a>
                              </li>
                              <li class="nav-item dropdown">
                                <a class="nav-link dropdown-toggle" href="http://example.com" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                  Dropdown link
                                </a>
                                <div class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                                  <a class="dropdown-item" href="#">Action</a>
                                  <a class="dropdown-item" href="#">Another action</a>
                                  <a class="dropdown-item" href="#">Something else here</a>
                                </div>
                              </li>
                            </ul>
                          </div>
                        </nav>
                        <div id="myCarousel" class="carousel slide" data-ride="carousel">
                          <!-- Indicators -->
                          <ol class="carousel-indicators">
                            <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
                            <li data-target="#myCarousel" data-slide-to="1"></li>
                            <li data-target="#myCarousel" data-slide-to="2"></li>
                          </ol>
                        
                          <!-- Wrapper for slides -->
                          <div class="carousel-inner">
                            <div class="item active">
                              <img src="{}">
                            </div>
                        
                            <div class="item">
                              <img src="{}">
                            </div>
                        
                            <div class="item">
                              <img src="{}">
                            </div>
                          </div>
                        
                          <!-- Left and right controls -->
                          <a class="left carousel-control" href="#myCarousel" data-slide="prev">
                            <span class="glyphicon glyphicon-chevron-left"></span>
                            <span class="sr-only">Previous</span>
                          </a>
                          <a class="right carousel-control" href="#myCarousel" data-slide="next">
                            <span class="glyphicon glyphicon-chevron-right"></span>
                            <span class="sr-only">Next</span>
                          </a>
                        </div>
                    </html>'''.format(url_for('static', filename='img/bird.jpeg'),
                                      url_for('static', filename='img/fox.jpg'), url_for('static',
                                                                                         filename='https://sweetpanda.ru/wp-content/uploads/2016/10/gettyimages-73726710.jpg'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
