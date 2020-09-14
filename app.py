from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/')
def home():
  return "Hello from Flask"

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
# Message Payload exemple:
#
#
#

@app.route('/gas', methods=['GET'])
def get_data_gas():
  return jsonify({'gas': "mygas"})
  #pass

if __name__=='__main__':
app.run(port=5000)
