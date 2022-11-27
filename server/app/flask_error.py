from server.app.flask_app import app


@app.errorhandler(404)
def not_found() -> str:
    return "404"


@app.errorhandler(400)
def bad_response() -> str:
    return "400"