import os

from app import create_app
from flask import Flask

from core.settings import Setting as ST

if __name__ == '__main__':
    app = create_app()
    if ST.DEBUG:
        app.run(port=ST.SERVER_PORT, host="0.0.0.0")
    else:
        app.run(port=ST.SERVER_PORT, host="127.0.0.1")

