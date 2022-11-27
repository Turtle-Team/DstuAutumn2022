from server.app import flask_app
import settings.flask

if __name__ == '__main__':
    flask_app.app.run(host=settings.flask.HOST_URL, port=5000)
