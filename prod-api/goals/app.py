from models import UserModel
from flask import Flask, request, jsonify
import json
import uuid
from datetime import datetime

app = Flask(__name__)
#app.debug = True 

def create_id():
    return str(uuid.uuid4())

@app.route('/goals', methods=['POST'])
def net_worth_save():
    goal_id = create_id()
    try:
        if request.method == 'POST':
            data = request.get_json()
            print (data)
            print (type(data))
            if not UserModel.exists():
                UserModel.create_table(read_capacity_units=1, write_capacity_units=1,wait=True)
            goal_data = UserModel(goal_id=goal_id,
                                  balances=data,
                                  name=
                                  account_id=
                                  account_type=
                                  subtype=
                                  goal_type=
                                  created_at=datetime.utcnow(),
                                  updated_at=datetime.utcnow())
            goal_data.save()
            return jsonify(data),201
    except Exception as e:
        return {'error':'Unable to save the net-worth - {}'.format(e)},500


@app.route('/goals/<goal_id>', methods=['GET','PUT','DELETE'])
def net_worth_get(goal_id):
    # try:
    if request.method == 'GET':
        user = UserModel.get(goal_id)
        user_dict = user.__dict__
        return jsonify(user_dict),200
    elif request.method == 'PUT':
        data = request.get_json()
        user = UserModel.get(goal_id)
        user.update(actions=[UserModel.balances.set(data.get("balances")),
                    UserModel.updated_at.set(datetime.utcnow())])
        return jsonify({"message":"successfully updated"}),200
    elif request.method == "DELETE":
        user = UserModel.get(goal_id)
        user.delete()
        return jsonify({"message":"successfully deleted"}),200
    # except Exception as e:
    #     return {'error': 'Unable to save the user - {}'.format(e)}, 500

if __name__ == '__main__':
    app.run()
