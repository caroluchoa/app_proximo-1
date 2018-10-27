
from flask import Flask, request, redirect, url_for, flash, render_template, jsonify
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from classes import Base, Restaurante, Refeicao, Cliente

engine = create_engine("mysql+mysqldb://root:password@localhost/app_proximo")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

#verdinho = classes.Restaurante("Verdinho")
#verdinho.incluir_prato()
#verdinho.incluir_bedida()

#spobreto = classes.Restaurante("Spobreto")
#spobreto.incluir_prato()
#spobreto.incluir_bebida()

#burguesao = classes.Restaurante("Burguesao")
#burguesao.incluir_prato()
#burguesao.incluir_bebida()



@app.route("/")
@app.route('/#')
@app.route('/restaurantes/')
def hello():
	restaurantes = session.query(Restaurante).all()
	return render_template('restaurante.html', restaurantes=restaurantes)


@app.route('/restaurantes/<int:restaurante_id>/')
@app.route('/restaurantes/<int:restaurante_id>/menu/')
def mostrarRestaurante(restaurante_id):
	restaurante = session.query(Restaurante).filter_by(id=restaurante_id).one()
	menu_restaurante = session.query(Refeicao).filter_by(restaurante_id=restaurante.id)
	return render_template('refeicao.html', restaurante=restaurante, menu_restaurante=menu_restaurante)



@app.route('/restaurantes/<int:restaurantes>/')
@app.route('/restaurantes/<int:restaurantes>/menu/')
def mostrarBebidas(restaurante_id):
	restaurante = session.query(Restaurante).filter_by(id=restaurante_id).one()
	menu_restaurante = session.query(Refeicao).filter_by(restaurante_id=restaurante.id)
	return render_template('refeicao.html', restaurante=restaurante, menu_restaurante=menu_restaurante)



@app.route("/pedido", methods=['POST'])
def pedido():

    restaurante_escolhido = request.form['lista_restaurantes']

    return render_template('refeicao.html', restaurante_escolhido=restaurante_escolhido)

@app.route("/ingrediente", methods=['POST'])
def ingrediente():

    refeicao_escolhida = request.form['refeicao']
    bebida_escolhida = request.form['bebida']

    return render_template('ingrediente.html', refeicao_escolhida=refeicao_escolhida,bebida_escolhida=bebida_escolhida)


@app.route("/dados", methods=['POST'])
def dados():
    
    refeicao_escolhida = request.form['refeicao_escolhida']
    bebida_escolhida = request.form['bebida_escolhida']

    arroz = request.form.get('arroz')
    if arroz:
        arroz = "arroz -"
    else:
        arroz = ""

    feijao = request.form.get('feijao')
    if feijao:
        feijao = "feijao -"
    else:
        feijao = ""

    tomate = request.form.get('tomate')
    if tomate:
        tomate = "tomate -"
    else:
        tomate = ""

    alface = request.form.get('alface')
    if alface:
        alface = "alface -"
    else:
        alface = ""

    batatafrita = request.form.get('batatafrita')
    if batatafrita:
        batatafrita = "batata frita -"
    else:
        batatafrita = ""

    ovofrito = request.form.get('ovofrito')
    if ovofrito:
        ovofrito = "ovo frito -"
    else:
        ovofrito = ""

    farofa = request.form.get('farofa')
    if farofa:
        farofa = "farofa -"
    else:
        farofa = ""

    cenoura = request.form.get('cenoura')
    if cenoura:
        cenoura = "cenoura -"
    else:
        cenoura = ""

    return render_template('dados.html', refeicao_escolhida=refeicao_escolhida, bebida_escolhida=bebida_escolhida, arroz=arroz, feijao=feijao, tomate=tomate, alface=alface, batatafrita=batatafrita,cenoura=cenoura,ovofrito=ovofrito,farofa=farofa)

@app.route("/fim", methods=['POST'])
def fim():
    return render_template('fim.html')

if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)

