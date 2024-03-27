from flask import Flask, request, url_for

app = Flask(__name__)


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
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.jpg')}" 
                            alt="здесь должна была быть картинка, но не нашлась">
                        <div class="alert alert-primary" role="alert">
                            Человечество вырастает из детства.
                        </div>
                        <div class="alert alert-success" role="alert">
                            Человечеству дана одна планета.
                        </div>
                    </html>"""


@app.route("/astronaut_selection", methods=['POST', 'GET'])
def form():
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
                                <title>Пример формы</title>
                              </head>
                              <body>
                                <h1>Анкета претендента</h1>
                                <h2>на участие в миссии</h2>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                        <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                        <input type="email" class="form-control" id="email" placeholder="Введите почту" name="email">
                                        <div class="form-group">
                                            <label for="gradeSelect">Какое у Вас образование</label>
                                            <select class="form-control" id="gradeSelect" name="class">
                                              <option>Начальное</option>
                                              <option>Среднее</option>
                                              <option>Высшее</option>
                                            </select>
                                        </div>
                                        <div class="form-group">
                                            <label for="form-check">Какие у Вас есть профессии?</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="engineer" value="engineer">
                                              <label class="form-check-label" for="engineer">
                                                Инженер
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="pilot" value="pilot">
                                              <label class="form-check-label" for="pilot">
                                                Пилот
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="checkbox" name="profession" id="builder" value="builder">
                                              <label class="form-check-label" for="builder">
                                                Строитель
                                              </label>
                                            </div>
                                        <div class="form-group">
                                            <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                            <textarea class="form-control" id="about" rows="4" name="about"></textarea>
                                        </div>
                                        
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['class'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])

        return "Форма отправлена"


@app.route("/choice/<string:planet>")
def choice(planet):
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                       <link rel="stylesheet"
                       href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                       integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                       crossorigin="anonymous">
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1>Моё предложение: {planet}</h1>
                        <h2>Планета близка к Земле</h2>
                        <div class="alert alert-primary" role="alert">
                          На ней много ресурсов
                        </div>
                        <div class="alert alert-success" role="alert">
                          Она красивая
                        </div>
                        <div class="alert alert-danger" role="alert">
                          И так далее...
                        </div>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
