from . import home_blueprint

@home_blueprint.route('/')
def index():
    return 'welcome to home page!'