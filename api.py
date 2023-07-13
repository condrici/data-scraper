"""
API Entry Point
This is the API entrypoint with all afferent routes
"""

import logging

import flask_api.status
from flask import Flask, jsonify, render_template
from flasgger import Swagger

from modules.DataScraper import PriceScraper
from modules.Schema import PriceSchema
from modules import Utilities

####################
# INITIALIZATION
####################

app = Flask(__name__)
Swagger(app, template=Utilities.get_json_from_file('documentation/swagger.json'))


@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):
    # defining function
    return render_template("404.html")


if __name__ != '__main__':
    raise Exception("Could not start server due to unknown application name")

Utilities.initiate_logging()

####################
# HTTP ROUTES
####################


@app.route('/scraper/<path:url>/<algorithm>', methods=['GET'])
def index(url: str, algorithm: str):
    try:
        price_schema = PriceScraper(url).scrape(algorithm)
    except BaseException as Ex:
        message = 'Something went wrong'
        Utilities.log(message + ' ' + str(Ex), logging.DEBUG)
        return jsonify(PriceSchema().dump(PriceSchema())), flask_api.status.HTTP_500_INTERNAL_SERVER_ERROR

    return jsonify(price_schema.dump(price_schema)), flask_api.status.HTTP_200_OK


####################
# START APPLICATION
####################


app.run(debug=True, port=8000, host="localhost")
