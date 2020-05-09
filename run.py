from flask import Flask, jsonify, render_template
from authlib.integrations.flask_client import OAuth
from loginpass import OAUTH_BACKENDS
from loginpass import create_flask_blueprint

if __name__ == '__main__':
    from templates import app
    #Load this config object for development mode
    app.config.from_object('configs.DevelopmentConfig')

    class Cache(object):
        def __init__(self):
            self._data = {}

        def get(self, k):
            return self._data.get(k)

        def set(self, k, v, timeout=None):
            self._data[k] = v

        def delete(self, k):
            if k in self._data:
                del self._data[k]

    # Cache is used for OAuth 1 services. You MUST use a real
    # cache service like memcache/redis on production.
    # THIS IS JUST A DEMO.
    oauth = OAuth(app, Cache())

    def handle_authorize(remote, token, user_info):
        user_info = jsonify(user_info)
        return user_info

    for backend in OAUTH_BACKENDS:
        bp = create_flask_blueprint(backend, oauth, handle_authorize)
        app.register_blueprint(bp, url_prefix='/{}'.format(backend.OAUTH_NAME))

    app.run()