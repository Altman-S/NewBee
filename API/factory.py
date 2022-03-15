from flask import Flask
from bson.json_util import ObjectId
import json
import os
from flask_cors import CORS


class MyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super(MyEncoder, self).default(obj)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, static_folder='../client/dist/static', template_folder="../client/dist", instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    """
    In a production environment, you should only allow cross-origin requests from the 
    domain where the front-end application is hosted. 
    Refer to the Flask-CORS documentation for more info on this
    """
    # CORS(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    # try:
        # os.makedirs(app.instance_path)
    # except OSError:
        # pass

    from flask import render_template 
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve(path):
        return render_template('index.html')

    app.json_encoder = MyEncoder

    from API.movies import movies_api
    app.register_blueprint(movies_api)

    return app
