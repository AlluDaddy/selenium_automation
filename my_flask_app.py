import logging

from flask import Flask, request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)

@app.route('/test', methods=['POST'])
def test():
    data = request.get_json()
    for xpath in data:
        app.logger.debug("Received XPath: %s", xpath)
    return "Received XPaths successfully", 200


if __name__ == '__main__':
    app.run()