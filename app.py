from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect ("/menu", code=302)
@app.route("/lab1")
def lab1():
    return '''
<!doctype html>
<html>
<link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
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
        веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        <div><a href="/menu">Меню</a></div>
        <h2>Реализованные роуты</h2>
        <div><a href="/lab1/oak">Дуб</a></div>
        <div><a href="/lab1/student">Студент</a></div>
        <div><a href="/lab1/python">Пайтон</a></div>
        <div><a href="/lab1/cat">Котик</a></div>
        <footer>
            &copy; Лабаскина София, Переладова Алёна, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
'''
@app.route("/menu")
def menu():
    return '''
<!doctype html>
<html>
<link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
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
'''
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
@app.route('/lab1/student')
def student():
    return '''
<!doctype html>
<html>
<link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>
        <h1>Студент: Лабаскина София, Переладова Алёна</h1>
        <img src="''' + url_for('static', filename='logo.png') + '''">
    </body>
</html>
'''
@app.route('/lab1/python')
def python():
    return '''
<!doctype html>
<html>
<link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>
        <h1>Знали ли вы?</h1>
        <div> Имя Python происходит от Монти Пайтона.
        Когда Гвидо ван Россум создавал Python, он также читал
        сценарии из "Летающего цирка Монти Пайтона".
        Он подумал, что такое имя было подходящим, коротким и немного загадочным.</div>
        <h1>Для чего используется Python?</h1>
        <div>Python обычно используется для разработки веб-сайтов
        и программного обеспечения, автоматизации задач,
        анализа данных и визуализации данных.
        Поскольку его относительно легко выучить, Python был принят многими
        непрограммистами, такими как бухгалтеры и ученые,
        для выполнения различных повседневных задач, 
        таких как организация финансов.</div>
        <img src="''' + url_for('static', filename='py.jpg') + '''">
    </body>
</html>
'''
@app.route('/lab1/cat')
def cat():
    return '''
<!doctype html>
<html>
<link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    <body>
        <h1>Знали ли вы?</h1>
        <div>Кошки хорошо ориентируются во вкусах, 
        различают кислое, горькое и солёное. 
        Разборчивость эта обусловлена, прежде всего, хорошим нюхом 
        и развитыми вкусовыми рецепторами на языке. Долгое время считалось, 
        что в отличие от большинства млекопитающих кошки не воспринимают
        сладкое, поскольку соответствующий ген у них повреждён, однако 
        последние исследования опровергли эту информацию.</h1>
        <div>Некоторые растения, например валериана или кошачья мята,
        выделяют вещества, которые обычно оказывают на кошек 
        (особенно на котов) воздействие, близкое к наркотическому. 
        Впрочем, не все кошки реагируют 
        на их запах, и не на всех кошек они оказывают одинаковое 
        воздействие. У некоторых кошек валериана может вызвать отравление.</div>
        <img src="''' + url_for('static', filename='cat.jpg') + '''">
    </body>
</html>
'''
@app.route('/lab2/example')
def example():
    name='Лабаскина София, Переладова Алёна'
    numberlaba = 'Лабораторная работа 2'
    return render_template('example.html', name=name, numberlaba=numberlaba)
    