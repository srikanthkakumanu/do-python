from bottle import Bottle, route, run, request, response, template, static_file, default_app

app = default_app()

# data
ninjas = [
    {
        'name': 'Yoshi',
        'belt_color': 'red',
        'speciality': 'Shadow Strike'
    },
    {
        'name': 'Hattori',
        'belt_color': 'green',
        'speciality': 'Tornado Blast'
    },
    {
        'name': 'Momochi',
        'belt_color': 'blue',
        'speciality': 'Rain Leap'
    }
]

@route('/public/<filename:path>')
def serve_static(filename):
    return static_file(filename, root='./static')

@route('/')
def home():
    return template('views/home.tpl', ninjas=ninjas)

# api endpoints
@route('/api/ninjas')
def get_ninjas():
    response.content_type = 'application/json'
    return {'data': ninjas}

@route('/api/ninjas', method='POST')
def add_ninja():
    """
    cURL command for POST request:

    curl -X POST -H "Content-Type: application/json" -d '{"name": "Bullet", "belt_color": "black", "speciality": "Bullet Time"}' http://localhost:8080/api/ninjas
    """
    new_ninja = request.json
    if isinstance(new_ninja, dict):
        ninjas.append(new_ninja)
        response.status = 201
    else:
        response.status = 400
    response.content_type = 'application/json'
    return {'message': 'Ninja added successfully', 'data': new_ninja}


def main():
    run(host='localhost', port=8080, debug=True, reloader=True)

if __name__ == '__main__':
    main()