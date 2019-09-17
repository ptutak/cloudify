from amartus import main_app, register, request

@main_app.route('/ztp/register/<id>', methods=['PUT'])
def index(id):
    register[id] = request.data
    return "{}".format(register[id])

#@main_app.route('/ztp/check/{id}')
#@main_app.route('/ztp/mng/list')
#@main_app.route('/ztp/mng/{id}/delete')
#@main_app.route('/ztp/mng/{id}')
