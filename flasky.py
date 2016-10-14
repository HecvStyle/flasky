from flask import Flask
from flask import render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    print(e)
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run()
