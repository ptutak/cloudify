from flask import Flask, request
from amartus import register

main_app = Flask(__name__)
main_app_register = register.Register()

from amartus import routes
