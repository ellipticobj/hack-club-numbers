from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

print("This python file is for the server\nPlease run client.py")

app = Flask(__name__)

numbers = []

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///numbers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Number(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer, nullable=True)

with app.app_context():
    db.create_all()


@app.route('/', methods=["POST"])
def addnumber():
    print("receiving number from client...")
    data = request.json
    number = data.get('number')
    
    if number is not None:
        newnumber = Number(value=number)
        db.session.add(newnumber)
        db.session.commit()
        return jsonify({"message": "number added successfully"}), 200
    return jsonify({'error': 'no number provided'}), 400

@app.route("/", methods=["GET"])
def getnumbers():
    print("sending numbers to client...")
    numbers = Number.query.all()
    numberslist = [num.value for num in numbers]
    return jsonify({'numbers': numberslist}), 200

if __name__ == '__main__':
    app.run(debug=True)
