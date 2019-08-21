from flask import Flask
app = Flask(__name__)
app.debug = True

if __name__ == '__main__':
    app.run()


@app.route('/')
def index():
    return 'INDEX'


if __name__ == '__main__':
    app.run()
