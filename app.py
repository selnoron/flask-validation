# Flask
import flask

app: flask.app.Flask = flask.Flask(__name__)

@app.route('/')
def main_page():
    return flask.render_template(
        'index.html'
    )

if __name__ == '__main__':

    app.run(
        host='localhost',
        port=8080,
        debug=True
    )