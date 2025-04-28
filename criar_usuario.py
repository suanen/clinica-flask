from app import app, db, Usuario
from werkzeug.security import generate_password_hash

# Criar a senha com hash
senha_hash = generate_password_hash('1234')

# Criar o novo usuário com senha criptografada
with app.app_context():
    usuario = Usuario(login='admin', senha=senha_hash)
    db.session.add(usuario)
    db.session.commit()

print("Usuário admin criado com sucesso!")

