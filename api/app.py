from flask import Flask, jsonify 
from api.__init__ import create_app
from api.models.models import db, Users
app = create_app()


@app.route('/', methods=['GET'])
def hello():
    users = Users.query.all()
    print(users)
    return jsonify({'success': True, 'data': [user.serialize() for user in users]}), 200


if __name__ == 'main':
    app.run(debug=True)