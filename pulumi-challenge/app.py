from flask import Flask
from tasks import tasks 
from config import Config # Import the tasks Blueprint

app = Flask(__name__)

app.config['SECRET_KEY'] = Config.SECRET_KEY

# Register the tasks Blueprint
app.register_blueprint(tasks, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
