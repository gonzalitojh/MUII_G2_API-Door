#!/usr/bin/env python3

import connexion
from flask_sqlalchemy import SQLAlchemy
from swagger_server import encoder

db = SQLAlchemy()

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Door Management API'}, pythonic_params=True)
    app.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tgglsmnhnqmtcw:43cb713a679612c64051103450311acd6556e12d989697f8c6ff1ab033c082ce@ec2-54-247-94-127.eu-west-1.compute.amazonaws.com:5432/dk7sdk7pf9j6c'
    db = SQLAlchemy(app.app)
    db.init_app(app.app)
    # Create the tables with the application context
    with app.app.app_context():
        db.create_all()

    app.run(port=8080)


if __name__ == '__main__':
    main()
