from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect ("/menu", code=302)
@app.route("/lab1")
def lab1():
    return """
<!doctype html>
<html>
    <head>
        <title> Лабаскина София, Переладова Алёна, Лабораторная 1 </title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h1>
        Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов
        веб-приложений, сознательно предоставляющих лишь самые ба-
        зовые возможности.

        <footer>
            &copy; Лабаскина София, Переладова Алёна, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
"""
@app.route("/menu")
def menu():
    return """
<!doctype html>
<html>
    <head>
        <title> Лабаскина София, Переладова Алёна, Лабораторная 1 </title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервер на flask</h1>
        Меню
        <footer>
            &copy; Лабаскина София, Переладова Алёна, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
"""
@app.route('/lab1/oak')
def oak():
    return '''
<!doctype html>
<html>
 <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''">
    </body>
</html>
'''
