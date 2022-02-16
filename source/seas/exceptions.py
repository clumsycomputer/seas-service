from rest_framework.views import exception_handler


def validation_exception_handler(someException, context):
    exception_response = exception_handler(someException, context)
    if type(someException).__name__ == "ValidationError":
        exception_response.data = {"validation_error": exception_response.data}
    return exception_response
