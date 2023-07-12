from app.common.exception.exceptions import (
    NotFoundException,
    BadRequestException,
    NotClassificationException,
)


def error_handle(app):
    @app.errorhandler(NotFoundException)
    def not_found_error(e):
        return e.to_json(), e.status_code

    @app.errorhandler(BadRequestException)
    def bad_request_error(e):
        return e.to_json(), e.status_code

    @app.errorhandler(NotClassificationException)
    def not_classification_error(e):
        return e.to_json(), e.status_code
