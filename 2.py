from flask import Flask

app = Flask("app")


@app.route('/')
def index():
    return f"""
    <!doctype html>
    <html>
        <head>
        </head>
        <body>
            <h1>Миссия Колонизации Марса<h1>
        </body>
    </html>
            """


@app.route('/index')
def _index():
    return f"""
    <!doctype html>
    <html>
        <head>
        </head>
        <body>
            <h1>И на Марсе будут яблони цвести!<h1>
        </body>
    </html>
            """


@app.route('/promotion')
def promotion():
    return f"""
    <!doctype html>
    <html>
        <head>
            <h1>Рекламная кампания<h1>
        </head>
        <body>
            <h1>Человечество вырастает из детства.<h1>
            <h1>Человечеству мала одна планета.<h1>
            <h1>Мы сделаем обитаемыми безжизненные пока планеты.<h1>
            <h1>И начнем с Марса!<h1>
            <h1>Присоединяйся!<h1>
        </body>
    """


@app.route('/image_mars')
def image():
    return f"""
    <!doctype html>
    <html>
        <head>
            <title>Привет, Марс!</title>
        </head>
        <body>
            <h1>Жди нас, Марс!<h1>
            <img src="static/imagees/MARS.png">
            <h6>Вот она какая, красная планета<h6>
    """


app.run(debug=True, port=8080)
