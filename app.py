from flask import Flask, render_template

app = Flask(__name__, static_folder='static_index', template_folder='templates')

# Página principal
@app.route('/')
def index():
    return render_template('index.html')

# Rutas de categorías
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

# Combinador
@app.route('/combinar')
def combinar():
    return render_template('combinar.html')

# 🔥 Nueva ruta: Asesoría
@app.route('/asesoria')
def asesoria():
    return render_template('asesoria.html')

# 🔥 Nueva ruta: Simulador
@app.route('/simulador')
def simulador():
    return render_template('simulador.html')

# 🔥 Nueva ruta: Envíos
@app.route('/envios')
def envios():
    return render_template('envios.html')


if __name__ == '__main__':
    app.run(debug=True)
