from flask import Flask

main_app = Flask(__name__)

from amartus.amartus import routes
