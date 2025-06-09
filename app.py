from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

estado = {
    "temperatura": None,
    "humidade": None,
    "chama": None,
    "alerta": False,
    "led": False,
    "buzzer": False
}

API_KEY = "123456"

@app.route("/", methods=["GET"])
def dashboard():
    return render_template("index.html", estado=estado)

@app.route("/dados", methods=["POST"])
def receber_dados():
    if request.headers.get("Authorization") != f"Bearer {API_KEY}":
        return jsonify({"erro": "Não autorizado"}), 401

    dados = request.json
    estado.update(dados)
    return jsonify({"mensagem": "Dados recebidos com sucesso"}), 200

@app.route("/comando", methods=["POST"])
def comando():
    acao = request.json
    estado["led"] = acao.get("led", estado["led"])
    estado["buzzer"] = acao.get("buzzer", estado["buzzer"])
    return jsonify({"mensagem": "Comando atualizado"}), 200

if __name__ == "__main__":
    app.run(debug=True)
