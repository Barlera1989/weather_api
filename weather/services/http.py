from http import HTTPStatus

def build_api_response(http_status):
    return build_response_message(http_status), http_status


def build_response_message(http_status):
    messages = {
        HTTPStatus.BAD_REQUEST: 'Bad Request',
        HTTPStatus.OK: 'OK',
    }

    return {'message': messages[http_status]}
