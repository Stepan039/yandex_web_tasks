from flask import Flask, request, url_for
import os

app = Flask(__name__)
photo = None


@app.route('/')
def mars():
    return "Миссия Колонизация Марса"


@app.route('/index')
def mars_anthem():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promo():
    return '</br>'.join(["Человечество вырастает из детства.",
                         "Человечеству мала одна планета.",
                         "Мы сделаем обитаемыми безжизненные пока планеты.",
                         "И начнем с Марса!",
                         "Присоединяйся!"])


@app.route('/image_mars')
def image():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                      </body>
                    </html>"""


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def rating(nickname, level, rating):
    return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                           <link rel="stylesheet"
                           href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                           integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                           crossorigin="anonymous">
                            <title>Результаты</title>
                          </head>
                          <body>
                            <h1>Результаты отбора</h1>
                            <h2>Претендент: {nickname}</h2>
                            <div class="alert alert-success" role="alert">
                              Ваш рейтинг после {level} этапа:
                            </div>
                            <div class="alert alert-secondary" role="alert">
                              составляет {rating}
                            </div>
                            <div class="alert alert-warning" role="alert">
                              Удачи!
                            </div>
                          </body>
                        </html>'''


@app.route('/load_photo', methods=['POST', 'GET'])
def sample_file_upload():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример загрузки файла</title>
                          </head>
                          <body>
                            <h1>Загрузка фотографии</h1>
                            <h2>Для участия в миссии</h2>
                            <div class="alert alert-success" role="alert">
                                <form method="post" enctype="multipart/form-data" id="photo_form">
                                  <label for="photo_form">Приложите фотографию</label>
                                  <div class="form-group">
                                      <input type="file" class="form-control-file" id="photo" name="file">
                                  </div>
                                  <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                                <img src="{url_for('static', filename='img/photo.jpg')}" 
           alt="  вы ещё не загрузили картинку">
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        photo = request.files['file']
        photo.save("static/img/photo.jpg")
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
