from werkzeug.wrappers import Request,Response

def application(environ,start_response):
    request=Request(environ=environ)
    text = 'Hello %s!'%request.args.get('name','world')
    response = Response(text,mimetype='text/plain')
    return response(environ,start_response)