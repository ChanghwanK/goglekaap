from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    print('run')
    app.run(debug=True)
