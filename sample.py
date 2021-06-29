from flask import Flask, json

employees = [{"id": 1, "name": "Employee1"}, {"id": 2, "name": "Employee2"}, {"id": 3, "name": "Employee3"}]

api = Flask(__name__)

@api.route('/employees', methods=['GET'])
def get_companies():
  return json.dumps(employees)

if __name__ == '__main__':
    api.run(host="{IP}")