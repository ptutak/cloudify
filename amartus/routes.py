from amartus import main_app, main_app_register, request


@main_app.route('/ztp/register/<id>', methods=['PUT'])
def index(id):
    main_app_register.register(
        id,
        request.form['ip'],
        request.form['name'],
        request.form['userdata'])
    return "{}".format(id)


#@main_app.route('/ztp/check/{id}')
#@main_app.route('/ztp/mng/list')
#@main_app.route('/ztp/mng/{id}/delete')
#@main_app.route('/ztp/mng/{id}')
