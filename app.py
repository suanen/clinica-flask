from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Inicializando o Flask
app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinica.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializando o banco de dados
db = SQLAlchemy(app)

# Modelos do banco
class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    telefone = db.Column(db.String(15), nullable=True)

class Consulta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'), nullable=False)
    data = db.Column(db.String(10), nullable=False)
    horario = db.Column(db.String(5), nullable=False)
    descricao = db.Column(db.Text, nullable=True)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

# Criando as tabelas no banco de dados
with app.app_context():
    db.create_all()

# Rotas da API
@app.route('/')
def home():
    return 'API Clínica Rodando!'

@app.route('/pacientes', methods=['POST'])
def cadastrar_paciente():
    dados = request.get_json()
    novo_paciente = Paciente(
        nome=dados['nome'],
        cpf=dados['cpf'],
        telefone=dados.get('telefone')
    )
    db.session.add(novo_paciente)
    db.session.commit()
    return jsonify({'mensagem': 'Paciente cadastrado com sucesso!'})

@app.route('/consultas', methods=['GET'])
def listar_consultas():
    consultas = Consulta.query.all()
    lista_consultas = []
    for consulta in consultas:
        paciente = Paciente.query.get(consulta.paciente_id)
        lista_consultas.append({
            'id': consulta.id,
            'paciente': paciente.nome if paciente else 'Desconhecido',
            'data': consulta.data,
            'horario': consulta.horario,
            'descricao': consulta.descricao
        })
    return jsonify(lista_consultas)

@app.route('/consultas', methods=['POST'])
def cadastrar_consulta():
    dados = request.get_json()
    nova_consulta = Consulta(
        paciente_id=dados['paciente_id'],
        data=dados['data'],
        horario=dados['horario'],
        descricao=dados.get('descricao')
    )
    db.session.add(nova_consulta)
    db.session.commit()
    return jsonify({'mensagem': 'Consulta cadastrada com sucesso!'})

@app.route('/login', methods=['POST'])
def login():
    dados = request.get_json()
    usuario = Usuario.query.filter_by(login=dados['login']).first()

    if usuario and check_password_hash(usuario.senha, dados['senha']):
        return jsonify({'mensagem': 'Login realizado com sucesso!'})
    else:
        return jsonify({'mensagem': 'Usuário ou senha inválidos'}), 401

# Rodar o servidor
if __name__ == '__main__':
    app.run(debug=True)