#http://werkzeug.pocoo.org/docs/0.11/routing/
#http://python.jobbole.com/87753/


#here use the redefine Map
#from here we could see endpoint is a String type.

from werkzeug.routing import Map, Rule, NotFound, RequestRedirect, HTTPException
url_map = Map([
    Rule('/', endpoint='blog/index'),
    Rule('/<int:year>/', endpoint='blog/archive'),
    Rule('/<int:year>/<int:month>/', endpoint='blog/archive'),
    Rule('/<int:year>/<int:month>/<int:day>/', endpoint='blog/archive'),
    Rule('/<int:year>/<int:month>/<int:day>/<slug>',
         endpoint='blog/show_post'),
    Rule('/about', endpoint='blog/about_me'),
    Rule('/feeds/', endpoint='blog/feeds'),
    Rule('/feeds/<feed_name>.rss', endpoint='blog/show_feed')
])
def application(environ, start_response):
    urls = url_map.bind_to_environ(environ)
    try:
        endpoint, args = urls.match()
    except HTTPException:
        return HTTPException(environ, start_response)
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return  ['Rule points to %r with arguments %r' % (endpoint, args)]
if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, application)

