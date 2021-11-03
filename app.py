from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta_hidden_track

@app.route('/')
def home():
    return render_template('signup.html')

@app.route('/sign', methods=['GET'])
def show_diary():
    sample_receive = request.args.get('sample_give')
    print(sample_receive)
    return jsonify({'msg': 'GET 연결 완료!'})

@app.route('/sign', methods=['POST'])
def save_diary():
    name_receive = request.form['name_give']
    memberid_receive = request.form['memberid_give']
    pw_receive = request.form['pw_give']
    reenter_receive = request.form['reenter_give']

    doc = {
        'name': name_receive,
        'memberid': memberid_receive,
        'pw': pw_receive,
        'reenter': reenter_receive
    }

    db.sign.insert_one(doc)

    return jsonify({'msg': '가입 완료!'})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)