from flask import Flask, Response, request
from stat import S_ISREG, ST_CTIME, ST_MODE
from hashlib import sha1
from shutil import rmtree
import random
import json
import os
from html_var import hello_html, login_ok, image_upload
from upload_image import broadcast, save_normalized_image, safe_addr, receive, event_stream
MAX_IMAGES = 10
DATA_DIR = 'data'
user = {'name': 'orhan', 'pw': '12345'}
app = Flask(__name__, static_folder=DATA_DIR)
try:  # Reset saved files on each start
    # rmtree(DATA_DIR, True)
    os.mkdir(DATA_DIR)
except OSError:
    pass


@app.route('/post', methods=['POST'])
def post():
    """Handle image uploads."""
    sha1sum = sha1(request.data).hexdigest()
    target = os.path.join(DATA_DIR, '{}.jpg'.format(sha1sum))
    message = json.dumps({'src': target,
                          'ip_addr': safe_addr(request.access_route[0])})
    try:
        if save_normalized_image(target, request.data):
            broadcast(message)  # Notify subscribers of completion
    except Exception as exception:  # Output errors
        return '{}'.format(exception)
    return 'UPLOAD SUCCESSFULLY COMPLETED'


@app.route('/image')
def home():
    """Provide the primary view along with its javascript."""
    # Code adapted from: http://stackoverflow.com/questions/168409/
    image_infos = []
    for filename in os.listdir(DATA_DIR):
        filepath = os.path.join(DATA_DIR, filename)
        file_stat = os.stat(filepath)
        if S_ISREG(file_stat[ST_MODE]):
            image_infos.append((file_stat[ST_CTIME], filepath))
    images = []
    for i, (_, path) in enumerate(sorted(image_infos, reverse=True)):
        if i >= MAX_IMAGES:
            os.unlink(path)
            continue
        images.append(f'<div><img alt="image is in :" src="{path}" /></div>')
    return image_upload  # % (MAX_IMAGES, '\n'.join(images))  # noqa


@app.route('/', methods=['GET'])
def hello():
    return hello_html


@app.route('/status', methods=['GET'])
def a_live():
    return "Alive!"


@app.route('/predict', methods=['POST'])
def predict():
    if request.form.get('month') != "" and request.form.get('customer_visiting_website') != "" and request.form.get('seller_available') != "":
        prediction = f'your prediction = {random.randint(2000, 5000)}'
        return prediction
    return "Please fill all 3 values"


@app.route('/login', methods=['POST'])
def login():
    name = request.form.get('user')
    pw = request.form.get('pass')
    if name == user['name'] and pw == user['pw']:
        return f"Login success for user {name} with password of length: {len(pw)}!" + login_ok
    return 'User name or password is not correct.'


@app.route('/stream')
def stream():
    """Handle long-lived SSE streams."""
    return Response(event_stream(request.access_route[0]),
                    mimetype='text/event-stream')


if __name__ == '__main__':
    app.run(debug=True, port=5001)  # run app in debug mode on port 5000
