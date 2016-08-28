from bottle import get, run

@get('/tags')
def ping():
    return {'tags': ["Fun", "Tech", "Social"]}

run(host='0.0.0.0', reloader=True, port=8888)
