from flask import Flask, request

main_app = Flask(__name__)

from amartus import routes, register

main_app_register = register.Register()
