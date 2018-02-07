from bottle import *
import os
import json

with open('bekkur.json', 'r' , encoding='utf-8') as f:
    bekkur = json.load(f)

@route('/')
def index():
    return template('index', bekkur=bekkur)

@route('/nemandi/<n>')
def nemandi(n):
    found = False
    for nemandi in bekkur['nemendur']:
        if nemandi['kt'] == n:
            return template('kt1',nemandi=nemandi)
            found = True
    if found == False:
        return error500()


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static_files')

@error(404)
def error404(error):
    return '<h1>Þessi síða er ekki til </h1>'

@error(500)
def error500(error):
    return '<h1>Þessi síða er ekki til </h1>'

run(host="0.0.0.0", port=os.environ.get('PORT'))
