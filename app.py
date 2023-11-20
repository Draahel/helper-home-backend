from config.db import app

from api.type import route_types
from api.user import route_users
from api.account import route_accounts
from api.publication import route_publications
from api.aplication import route_aplications
from api.stage import route_stages

app.register_blueprint(route_types, url_prefix = '/api')
app.register_blueprint(route_users, url_prefix = '/api')
app.register_blueprint(route_accounts, url_prefix = '/api')
app.register_blueprint(route_publications, url_prefix = '/api')
app.register_blueprint(route_aplications, url_prefix = '/api')
app.register_blueprint(route_stages, url_prefix = '/api')


@app.route('/api')
def index():
    return "Hola Mundo"

# @app.route('/dostablas', methods=['GET'])
# def dostabla():
#     datos = {}
#     resultado = db.session.query(Cliente, Reserva). \
#         select_from(Cliente).join(Reserva).all()
#     i=0
#     for clientes, reservas in resultado:
#         i+=1
#         datos[i]={
#             'cliente':clientes.nombre,
#             'reserva': reservas.id
#         }
#     return datos

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')