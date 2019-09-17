from flask import Flask, request

main_app = Flask(__name__)

register = {}

from amartus import routes
