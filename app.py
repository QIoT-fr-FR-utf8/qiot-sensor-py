from flask import Flask,jsonify,request
import gas_extend
import particules_extend
import os

app = Flask(__name__)

@app.route('/')
def index():
  result = {}
  result['result']="Hello QIoT"
  return jsonify(result)


@app.route('/api/sensors')
def listsensor():
  listofSensor=[]
  listofSensor.append('/api/sensors/gas')
  listofSensor.append('/api/sensors/pollution')

  result={}
  result={"result":listofSensor}

  return jsonify(result)

#get /api/gas
# Message type
# {
#   "stationId":int,
#   "instant":String*,
#   "adc":double,
#   "nh3":double,
#   "oxidising":double,
#   "reducing":double,
# }

@app.route('/api/sensors/gas', methods=['GET'])
def get_data_gas():
  result={}
  result={"result":gas_extend.json_parsing_return()}
  return jsonify(result)

@app.route('/api/sensors/particules', methods=['GET'])
def get_data_particules():
  result={}
  result={"result":particules_extend.json_parsing_return()}
  return jsonify(result)

if __name__=='__main__':
  app.run(host=os.getenv('FLASK_APP_HOST'),port=os.getenv('FLASK_APP_PORT'),debug=os.getenv('FLASK_APP_DEBUG'))
