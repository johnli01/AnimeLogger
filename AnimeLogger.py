from flask import Flask, request
from flask.globals import current_app
import requests
from backend.updater.MALUpdater import MALUpdater

app = Flask(__name__)
app.register_blueprint(MALUpdater, url_prefix="")


if __name__ == '__main__':
  app.run()