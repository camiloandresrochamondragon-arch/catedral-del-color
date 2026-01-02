from flask import Flask, render_template

app = Flask(__name__, static_folder='static_index', template_folder='templates')

# --------------------------
# Página principal
# --------------------------
@app.route('/')
def index():
    return render_template('index.html')

# --------------------------
# Rutas de categorías
# --------------------------
@app.route('/vinilos')
def vinilos():
    return render_template('vinilos.html')

@app.route('/madera')
def madera():
    return render_template('madera.html')

@app.route('/automotriz')
def automotriz():
    return render_template('automotriz.html')

@app.route('/lacas')
def lacas():
    return render_template('lacas.html')

@app.route('/ferreteria')
def ferreteria():
    return render_template('ferreteria.html')

@app.route('/combinar')
def combinar():
    return render_template('combinar.html')

@app.route('/asesoria')
def asesoria():
    return render_template('asesoria.html')

@app.route('/simulador')
def simulador():
    return render_template('simulador.html')

@app.route('/envios')
def envios():
    return render_template('envios.html')


# =======================================================
#                     PINTULAND
# =======================================================

@app.route("/pintuland/tipo1/galon")
def pintuland_tipo1_galon():
    return render_template("pintuland/tipo1/galon.html")

@app.route("/pintuland/tipo1/balde")
def pintuland_tipo1_balde():
    return render_template("pintuland/tipo1/balde.html")

@app.route("/pintuland/tipo1/caneca")
def pintuland_tipo1_caneca():
    return render_template("pintuland/tipo1/caneca.html")

@app.route("/pintuland/acriland/galon")
def pintuland_acriland_galon():
    return render_template("pintuland/acriland/galonacrilan.html")

@app.route("/pintuland/acriland/balde")
def pintuland_acriland_balde():
    return render_template("pintuland/acriland/baldeacriland.html")

@app.route("/pintuland/acriland/caneca")
def pintuland_acriland_caneca():
    return render_template("pintuland/acriland/canecaacriland.html")


# =======================================================
#                     RECOLTEX
# =======================================================
# =========================
#        RECOLTEX
# =========================

@app.route("/recoltex/tipo2/estandar")
def recoltex_tipo2_estandar():
    return render_template("recoltex/estandar/estandar.html")


@app.route("/recoltex/tipo2/superior")
def recoltex_tipo2_superior():
    return render_template("recoltex/superior/superior.html")


@app.route("/recoltex/hidroplast/hidroplast.html/")
def recoltex_hidroplast():
    return render_template("recoltex/hidroplast/hidroplast.html")

@app.route("/recoltex/vinicol")
def recoltex_vinicol():
    return render_template("recoltex/vinicol/vinicol.html")

@app.route("/recoltex/recolcryl/recolcryl.html")
def recoltex_resina_acrilica():
    return render_template("recoltex/recolcryl/recolcryl.html")

@app.route("/recoltex/recoltex_tipo1/galonrecoltex/")
def recoltex_tipo1_galonrecoltex():
    return render_template("recoltex/recoltex_tipo1/galonrecoltex.html")

@app.route("/recoltex/aquamel/aquamel.html")
def recoltex_tipo1_aquamel():
    return render_template("recoltex/aquamel/aquamel.html")

# =======================================================
#                     INDUPIN
# =======================================================

@app.route("/indupin/constructor/tipo1")
def indupin_constructor_tipo1():
    return render_template("indupin/constructor/tipo1constructor.html")

@app.route("/indupin/constructor/tipo2")
def indupin_constructor_tipo2():
    return render_template("indupin/constructor/tipo2constructor.html")

@app.route("/indupin/homeline/tipo1")
def indupin_homeline_tipo1():
    return render_template("indupin/homeline/tipo1.html")

@app.route("/indupin/homeline/tipo2")
def indupin_homeline_tipo2():
    return render_template("indupin/homeline/tipo2.html")


# =======================================================
#                     SAPOLIN
# =======================================================

@app.route("/sapolin/fachadassapolin/fachadassapolin.html")
def sapolin_fachadas():
    return render_template("sapolin/fachadassapolin/fachadassapolin.html")

@app.route("/sapolin/barnizagua/barnizagua.html")
def sapolin_barniz():
    return render_template("sapolin/barnizagua/barnizagua.html")
@app.route("/sapolin/invercril500/invercril500.html")
def sapolin_resina():
    return render_template("sapolin/invercril500/invercril500.html")


if __name__ == "__main__":
    app.run(debug=True)
