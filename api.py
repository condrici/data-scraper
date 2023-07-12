import flask_api.status
import logging
from flask import Flask, jsonify, render_template
from modules.DataScraper import PriceScraper
from modules import Utilities

app = Flask(__name__)

####################
# CONFIGURATION
####################


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
        scraped_price = PriceScraper(url).scrape(algorithm).get_price_whole_with_decimal()
    except BaseException as Ex:
        message = 'Something went wrong'
        Utilities.log(message + ' ' + str(Ex), logging.DEBUG)
        return jsonify({'message': message}), flask_api.status.HTTP_500_INTERNAL_SERVER_ERROR

    return jsonify({'message': scraped_price}), flask_api.status.HTTP_200_OK


####################
# START APPLICATION
####################


app.run(debug=True, port=8000, host="localhost")
