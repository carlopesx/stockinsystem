from flask import Flask, render_template, request, redirect, url_for
# Importa a sua classe do seu arquivo original (assumindo que o arquivo se chama produto.py)
from produto import Produto 

app = Flask(__name__)

# O seu estoque global que substitui o 'estoque = []' do terminal
estoque = []

# ROTA 1: Página Inicial (Seu Menu Principal + Listagem de Produtos)
@app.route("/")
def home():
    # Substitui a Opção 2 do menu. Sempre exibe a lista atualizada.
    return render_template("menuGUI.html", estoque=estoque, user="carlos")


# ROTA 2: Cadastrar Produto (Substitui a Opção 1)
@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    # Captura os dados enviados pelo formulário HTML (Substitui os inputs)
    tipo = request.form.get("tipo")
    id_prod = request.form.get("id")
    nome = request.form.get("nome")
    quantidade = request.form.get("quantidade")
    preco = request.form.get("preco")
    
    # Validação simples (Substitui as validações de .isdigit() do seu while)
    if not id_prod.isdigit() or not quantidade.isdigit() or not preco.isdigit():
        # Se algo estiver errado, recarrega a página passando um aviso
        return render_template("menuGUI.html", estoque=estoque, user="carlos", erro="Dados inválidos detectados!")

    # Cria o objeto usando a sua classe original e adiciona na lista
    novo_produto = Produto(tipo, id_prod, nome, int(quantidade), float(preco))
    estoque.append(novo_produto)
    
    # Redireciona de volta para o menu principal
    return redirect(url_for("home"))


# ROTA 3: Editar Produto (Substitui a Opção 3)
@app.route("/editar", methods=["POST"])
def editar():
    id_busca = request.form.get("id_busca")
    
    # Lógica de busca igual ao seu método 'editar_produto' original
    for produto in estoque:
        if str(produto.id) == id_busca:
            # Captura os novos campos informados na tela
            novo_nome = request.form.get("novo_nome") or None
            novo_tipo = request.form.get("novo_tipo") or None
            nova_qtd = request.form.get("nova_qtd")
            novo_preco = request.form.get("novo_preco")
            
            # Executa o seu método 'atualizar' já existente na classe Produto
            produto.atualizar(
                nome=novo_nome,
                tipo=novo_tipo,
                quantidade=int(nova_qtd) if nova_qtd else None,
                preco=float(novo_preco) if novo_preco else None
            )
            return redirect(url_for("home"))
            
    return render_template("menuGUI.html", estoque=estoque, user="carlos", erro=f"ID '{id_busca}' não encontrado.")

if __name__ == "__main__":
    app.run(debug=True)