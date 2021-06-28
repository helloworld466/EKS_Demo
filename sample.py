from flask import Flask, json

employees = [{"id": 1, "name": "AkshayBadri"}, {"id": 2, "name": "SwathiThangaraj"}]

api = Flask(__name__)

@api.route('/employees', methods=['GET'])
def get_companies():
  return json.dumps(employees)

if __name__ == '__main__':
    api.run(host="{IP}")
