#!/usr/bin/env python3

import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from swagger_server import encoder
from flask import Flask
import swagger_server.database as database
import swagger_server.commands as commands

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.config.from_object("config.DevelopmentConfig")
    # setup all our dependencies, for now only database using application factory pattern
    database.init_app(app.app)
    commands.init_app(app.app)

    app.run(port=8080)


if __name__ == '__main__':
    main()
