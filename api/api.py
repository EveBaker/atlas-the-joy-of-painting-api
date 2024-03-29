from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flast(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///joy_of_painting.db'
db = SQLAlchemy(app)

@app.route('/episodes', methods=['GET'])
def get_episodes();
return jsonify({'message': 'API endpoint for filtering episodes'})

if __name__ == '__main__':
    app.run(debug=True)