from amartus import main_app


@main_app.route('/zip/register/{id}')
@main_app.route('/ztp/check/{id}')
@main_app.route('/ztp/mng/list')
@main_app.route('/ztp/mng/{id}/delete')
@main_app.route('/ztp/mng/{id}')
def index():
    return "Hello World"
