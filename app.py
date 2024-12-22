from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "А теперь изменяем текст и ждём 2 минуты."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
