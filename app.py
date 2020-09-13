from flask import Flask,jsonify,request,render_template
import enviroplus

app = Flask(__name__)

@app.route('/')
def home():
  return "Hello from Flask"

#get /gas
@app.route('/gas')
def get_stores():
  return jsonify({'gas': "mygas"})
  #pass


app.run(port=5000)
