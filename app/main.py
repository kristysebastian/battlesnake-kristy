import bottle
import json


@bottle.get('/')
def index():
    return """
        <a href="https://github.com/sendwithus/battlesnake-python">
            battlesnake-python
        </a>
    """


@bottle.post('/start')
def start():
    data = bottle.request.json

    return json.dumps({
        'name': 'battlesnake-test',
        'color': '#00ff00',
        'head_url': 'http://battlesnake-python.herokuapp.com',
        'taunt': 'battlesnake-python!'
    })


@bottle.post('/move')
def move():
    data = bottle.request.json
    print data
    
    # Here is where you write your logic
    # Look at the data using the heroku logs thing you tried
    # Write some logic and return an up, left, right, or down

    return json.dumps({
        'move': 'left',
        'taunt': 'battlesnake-python!'
    })


@bottle.post('/end')
def end():
    data = bottle.request.json

    return json.dumps({})


# Expose WSGI app
application = bottle.default_app()
