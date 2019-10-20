def some_view(some_service, error_handler):
    try:
        some_service()
        return '', 200
    except Exception as e:
        return error_handler(e)
