import flask
import read

app = flask.Flask(__name__)

@app.route('/')

def hello():
    return flask.render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

