from flask import Blueprint,render_template
lab2 = Blueprint('lab2', __name__)

@lab2.route('/lab2/example')
def example():
    name, numberlaba, group, kurs ='Лабаскина София, Переладова Алёна', 'Лабораторная работа 2', 'ФБИ-12', '3 курс'
    fruits = [{'name':'яблочки', 'price': 100},
            {'name':'груши', 'price': 120},
            {'name':'апельсины', 'price': 80},
            {'name':'мандарины', 'price': 95}, {'name':'манго', 'price': 321}]
    books = [{'author':'Эрих Мария Ремарк','name':'Возлюби ближнего своего', 'zanr': 'фикшн', 'str': 480},
            {'author':'Эрих Мария Ремарк','name':'Триумфальная арка', 'zanr': 'роман', 'str': 640},
            {'author':'Виктор Пелевин','name':'Путешествие в Элевсин', 'zanr': 'роман', 'str': 480},
            {'author':'Михаил Булгаков','name':'Мастер и Маргарита', 'zanr': 'роман', 'str': 512},
            {'author':'Антон Павлович Чехов','name':'Вишневый сад', 'zanr': 'роман', 'str': 352},
            {'author':'Михаил Юрьевич Лермонтов','name':'Герой нашего времени', 'zanr': 'роман', 'str': 224},
            {'author':'Александр Сергеевич Грибоедов','name':'Горе от ума', 'zanr': 'роман', 'str': 256},
            {'author':'Александр Сергеевич Пушкин','name':'Гробовщик', 'zanr': 'роман', 'str': 16},
            {'author':'Александр Сергеевич Пушкин','name':'Выстрел', 'zanr': 'роман', 'str': 32},
            {'author':'Джордж Оруэлл','name':'Скотный двор', 'zanr': 'роман', 'str': 416}]
    return render_template('example.html',
                            name=name, numberlaba=numberlaba, group=group,kurs=kurs, fruits=fruits, books=books)
@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')
@lab2.route('/lab2/butterfly')
def butterfly():
    return render_template('butterfly.html')