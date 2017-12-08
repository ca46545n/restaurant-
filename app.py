from flask import Flask,jsonify
import json

app = Flask(__name__)
jData = json.loads(open('./resturant.json').read())
data=jData["Restaurant"]
# print (data[0]["id"])

@app.route('/')
def hello_world():
    return 'Flask Dockerized'

@app.route('/restaurant/')
@app.route('/restaurant/<string:id>/')
def hello_world1(id=''):
        if not id:
            v = 'for blank'
            print('for blank')
            rdata = jsonify(data)
        else:
            v = 'for not blank'
            print('for not blank')
            rdata = jsonify(v)
        for f in data:
            if f["id"] == id:
                rdata = jsonify(f)
        return rdata

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
