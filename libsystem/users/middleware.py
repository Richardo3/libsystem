
def my_middleware(get_response):
    print('init被调用')
    def middleware(request):
        print('before request 被调用')
        response = get_response(request)
        print('after request 被调用')
        return response
    return middleware