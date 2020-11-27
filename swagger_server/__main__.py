#!/usr/bin/env python3

import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from swagger_server import encoder
from flask import Flask

app = connexion.App(__name__, specification_dir='./swagger/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'Door Management API'}, pythonic_params=True)

if __name__ == "__main__":
    app.run(threaded=True, port=5000)