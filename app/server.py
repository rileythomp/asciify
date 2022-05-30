import flask
from flask_cors import CORS
from imgtoascii import ImgFileToAscii

app = flask.Flask(__name__, static_url_path='/static')
CORS(app)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def home():
    return flask.send_from_directory('static', 'index.html')

@app.route('/asciiart', methods=['POST'])
def asciiart():
    img = flask.request.files.get('image')
    try: 
        asciiart = ImgFileToAscii(img)
    except ValueError:
        print('Error converting image to ascii')
        response = app.response_class(
            response='Error converting image to ascii',
            status=500,
            mimetype='text/plain'
        )
        return response
    response = app.response_class(
        response=asciiart,
        status=200,
        mimetype='text/plain'
    )
    return response



# app.run(debug=True, port=5000)
