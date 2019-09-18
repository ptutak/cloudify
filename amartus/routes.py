import json
from urllib.request import urlopen
from urllib.error import URLError
from flask import jsonify, abort
from amartus import main_app, main_app_register, request


@main_app.route('/ztp/register/<id>', methods=['PUT'])
def register(id):
    try:
        data = json.loads(request.data.decode())
    except Exception:
        abort(400)
    try:
        main_app_register.register(
            id,
            data['ip'],
            data['name'],
            data['userdata'])
    except ValueError:
        abort(409)
    try:
        urlopen('http://adress/api/exec?ip={}'.format(data['ip']))
    except URLError:
        return jsonify({'register': "FAILED TO EXECUTE"})
    return jsonify({'register': 'SUCCESS'})


@main_app.route('/ztp/check/<id>', methods=['GET'])
def check(id):
    return jsonify(main_app_register.check(id))


@main_app.route('/ztp/mng/list', methods=['GET'])
def list_register():
    register_list = main_app_register.list_register()
    return jsonify({'hosts': register_list})


@main_app.route('/ztp/mng/<id>/delete', methods=['GET'])
def delete(id):
    main_app_register.delete(id)
    return jsonify({'delete': 'SUCCESS'})


@main_app.route('/ztp/mng/<id>', methods=['PUT'])
def edit(id):
    try:
        data = json.loads(request.data.decode())
    except Exception:
        abort(400)
    good_keys = {'ip', 'name', 'userdata'}
    if not good_keys >= set(data.keys()):
        abort(400)
    try:
        main_app_register.update(id, **data)
    except KeyError:
        abort(400)
    return jsonify(main_app_register.check(id))
