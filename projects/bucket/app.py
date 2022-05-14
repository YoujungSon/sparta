from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
# mongo DB
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.7zzzx.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')
# 기록하기
@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']
    # DB 가져오기
    bucket_list = list(db.bucket.find({}, {'_id': False}))
    # 리스트 갯수 세기
    count = len(bucket_list) + 1
    # DB 저장
    doc = {
        'num': count,
        'bucket': bucket_receive,
        'done': 0
    }
    db.bucket.insert_one(doc)
    return jsonify({'msg': '등록 완료!'})

@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    num_receive = request.form['num_give']
    db.bucket.update_one({'num': int(num_receive)}, {'$set': {'done': 1}})
    return jsonify({'msg': '버킷 완료!'})
@app.route("/bucket/cancel", methods=["POST"])
def cancel_done():
    num_receive = request.form['num_give']
    db.bucket.update_one({'num': int(num_receive)}, {'$set': {'done': 0}})
    return jsonify({'msg': '취소!'})
# 보여주기
@app.route("/bucket", methods=["GET"])
def bucket_get():
    # DB 가져오기
    bucket_list = list(db.bucket.find({}, {'_id': False}))
    return jsonify({'buckets': bucket_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)