from flask import Flask, render_template, jsonify, request, redirect, session, url_for
from requests import get
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Замените на свой секретный ключ
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Используем SQLite для простоты, можно заменить на другую БД
db = SQLAlchemy(app)

@app.route('/scores', methods=['GET'])
def get_scores():
    try:
        response = get("http://193.164.149.85:5000/scores")
        result = response.json()[0]
        return jsonify(result)
    except Exception as e:
        print(e)
        return jsonify({"error": "Error fetching data"})

@app.route('/')
def home():
    response = get("http://193.164.149.85:5000/scores")
    result = response.json()[0]
    return render_template('redir.html', result=result)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Создание всех таблиц в базе данных
# db.create_all()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Проверяем, есть ли пользователь с таким именем уже в базе
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            # return 'Пользователь с таким именем уже существует!'
            return render_template("somethingwentwrong.html")
        
        # Хэшируем пароль
        # hashed_password = generate_password_hash(password, method='sha256')
        hashed_password = generate_password_hash(password, method='pbkdf2:sha1', salt_length=8)
        
        # Создаем нового пользователя
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Проверяем, существует ли пользователь с таким именем
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            # Если пользователь существует и пароль совпадает, авторизуем его
            session['username'] = username
            return redirect(url_for('index'))
        
        return 'Неверное имя пользователя или пароль!'

    return render_template('login.html')

@app.route('/logout')
def logout():
    # Удаляем пользователя из сессии, выход из учетной записи
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/index')
def index():
    response = get("http://193.164.149.85:5000/scores")
    result = response.json()[0]
    return render_template('home.html', result=result)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
