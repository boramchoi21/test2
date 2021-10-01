from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.dbStock


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/memo', methods=['POST'])
def save_post():
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']
    reg_date_receive = request.form['reg_date_give']

    doc = {
        'title':title_receive,
        'content':content_receive,
        'reg_date':reg_date_receive,
    }

    db.users.insert_one(doc)

    return jsonify({'msg':'저장완료!'})


@app.route('/memo', methods=['GET'])
def get_post():
    memo_receive = list(db.users.find({}, {'_id': False}))
    print(sample_receive)

    return jsonify({'all_memos':memo_receive})




@app.route('/post', methods=['DELETE'])
def delete_post():
    return {"result": "success"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
