from flask import Flask, render_template
from controllers import routes
from models.database import mongo, Game

app = Flask(__name__, template_folder='views')
routes.init_app(app)

# Definindo o endereço do MongoDB
app.config['MONGO_URI'] = 'mongodb://localhost:27017/games'

if __name__ == '__main__':
    mongo.init_app(app=app)
    # Adiciona um documento a coleção ao iniciar a aplicação
    with app.app_context():
        # Para a coleção 'games' faz a criação caso não exista
        if 'games' not in mongo.db.list_collection_names():
            # Insere um documento para criar a coleção
            game = Game(
                titulo='',
                ano=0,
                categoria='',
                plataforma='',
                preco=0,
                quantidade=0
            )
            game.save()
    app.run(host='localhost', port=5000, debug=True) 