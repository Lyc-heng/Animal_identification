import flask
import system

app = flask.Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/infer', methods=['GET'])
def infer():
    text = flask.request.args.get('q', '')
    dis = flask.request.args.get('display', '')
    result = system.run(text, dis)
    return result


if __name__ == '__main__':
    app.run()
