from flask import Flask
from controllers.atividade_controller import atividade_bp

app = Flask(__name__)

app.register_blueprint(atividade_bp, url_prefix='/atividades')

if __name__ == '__main__':
    app.run(debug=True)
