import flask
import read

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def first():
    if flask.request.method == 'POST':
        return flask.redirect('/second')

    return flask.render_template('index.html', first=True, second=False, third=False, fourth=False, fifth=False, sixth=False)

@app.route('/second', methods=['GET', 'POST'])
def second():
    if flask.request.method == 'POST':
        return flask.redirect('/third')

    return flask.render_template('index.html', first=False, second=True, third=False, fourth=False, fifth=False, sixth=False)

@app.route('/third', methods=['GET', 'POST'])
def third():
    if flask.request.method == 'POST':
        return flask.redirect('/fourth')

    return flask.render_template('index.html', first=False, second=False, third=True, fourth=False, fifth=False, sixth=False)

@app.route('/fourth', methods=['GET', 'POST'])
def fourth():
    if flask.request.method == 'POST':
        return flask.redirect('/fifth')

    return flask.render_template('index.html', first=False, second=False, third=False, fourth=True, fifth=False, sixth=False)


@app.route('/fifth', methods=['GET', 'POST'])
def fifth():
    if flask.request.method == 'POST':
        return flask.redirect('/sixth')

    return flask.render_template('index.html', first=False, second=False, third=False, fourth=False, fifth=True, sixth=False)

@app.route('/sixth', methods=['GET', 'POST'])
def sixth():
    return flask.render_template('index.html', first=False, second=False, third=False, fourth=False, fifth=False, sixth=True)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

