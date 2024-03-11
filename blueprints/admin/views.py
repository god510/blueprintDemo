from . import admin_blueprint

@admin_blueprint.route('/')
def index():
    return 'welcome to admin page!'

@admin_blueprint.route('/test')
def test11():
    return 'welcome to admin/test page!'