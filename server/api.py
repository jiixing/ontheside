from flask.ext.restless import ProcessingException
from forms import RegistrationForm
from models import User, Keyword, Language, Project


def validate_with_form(form_class):
    def preprocessor(data=None):
        form = form_class.from_json(data)
        if not form.validate():
            raise ProcessingException

    return preprocessor


def remove_props(props):
    def preprocessor(data=None):
        for prop in props:
            del data[prop]

    return preprocessor

api_config = [
    {
        'model': User,
        'methods': ['GET', 'POST', 'DELETE'],
        'preprocessors': {
            'POST': [
                validate_with_form(RegistrationForm),
                remove_props(['confirm'])
            ]
        }
    },
    {
        'model': Keyword,
        'methods': ['GET', 'POST', 'DELETE']
    },
    {
        'model': Language,
        'methods': ['GET', 'POST', 'DELETE']
    },
    {
        'model': Project,
        'methods': ['GET', 'POST', 'DELETE'],
        'include_columns': ['id', 'description',
                            'source', 'type']
    }
]
