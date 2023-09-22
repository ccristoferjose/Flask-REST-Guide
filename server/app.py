from flask import Flask, request, jsonify
from data import estudiantes

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/estudiantes', methods=['GET'])
def get_estudiantes():
    return jsonify({'Estudaintes': estudiantes})

@app.route('/estudiantes/<int:id>', methods=['GET'])
def get_estudiante(id):
    estudiante = next((item for item in estudiantes if item['id'] == id), None)
    if estudiante is None:
        return jsonify({'message': 'Estudiante no encontrado'}), 404
    return jsonify({'Estudiante': estudiante}), 200

@app.route('/estudiantes', methods=['POST'])
def add_estudiante():
    campos_requeridos = ['id', 'nombre', 'apellido', 'edad', 'carrera']
    for campo in campos_requeridos:
        if campo not in request.json:
            return jsonify({'error': f'Campo {campo} faltante'}), 400
    estudiante = {
        'id': request.json['id'],
        'nombre': request.json['nombre'],
        'apellido': request.json['apellido'],
        'edad': request.json['edad'],
        'carrera': request.json['carrera']
    }
    estudiantes.append(estudiante)
    with open('data.py', 'w') as f:
        f.write(f'estudiantes = {estudiantes}')

    return jsonify(estudiantes), 200


def actualizar_data():
    with open('data.py', 'w') as f:
        f.write(f'estudiantes = {estudiantes}')

@app.route('/estudiantes/<int:estudiante_id>', methods=['PUT'])
def update_estudiante(estudiante_id):
    estudiante = next((item for item in estudiantes if item['id'] == estudiante_id), None)
    if estudiante is None:
        return jsonify({'error': 'Estudiante no encontrado'}), 404
    data = request.json
    estudiante.update(data)
    
    actualizar_data() 

    return jsonify({'estudiante': estudiante})


@app.route('/estudiantes/<int:estudiante_id>', methods=['DELETE'])
def delete_estudiante(estudiante_id):
    global estudiantes
    estudiantes = [item for item in estudiantes if item['id'] != estudiante_id]
    
    actualizar_data()  # Actualiza el archivo `data.py`

    return jsonify(estudiantes)



if __name__ == '__main__':
    app.run(debug=True, port=5000)