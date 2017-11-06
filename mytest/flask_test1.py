from flask import Flask
#use gunicorn name:appName to start
#example gunicorn flask_test1:app
#visiti http://localhost:8000/
app = Flask(__name__)

@app.route('/')
def hell_world():
    return 'Hello,World!'

if __name__ == '__main__':
    app.run()