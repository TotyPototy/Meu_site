from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    """
    <h1>Seja bem-vindo ao meu Mini-Site!!</h1>
    <p>Use a barra de endereços para navegar:</p> 
    <ul>
      <li>/sobre</li>
      <li>/contato</li>
      <li>/perfil</li>
    </ul>
    """

@app.route("/sobre")
def sobre():
    return "<h1>Sobre nós</h1><p>Esta é a página sobre... nós!!</p>"

@app.route("/contato")
def contato():
    return "<h1>Contato</h1><p>Nosso e-mail é aluno@escola.com</p>"

@app.route("/perfil/<nome>")
def perfil(nome):
    return render_template("perfil.html", nome_do_usuario=nome)
    return f"<h1>Olá, {nome}!!</h1><p>Este é o seu perfil!!</p>"

if __name__ == "__main__":
    app.run(debug=True)