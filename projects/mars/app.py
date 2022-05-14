from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.7zzzx.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

# HTML 연결
@app.route('/')
def home():
    return render_template('index.html')

# 주문 저장하기
@app.route("/mars", methods=["POST"])
def web_mars_post():
    # 입력 요청
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']
    # 리스트 만들기
    doc = {
        'name': name_receive,
        'address': address_receive,
        'size': size_receive
    }
    # DB에 저장
    db.mars.insert_one(doc)
    return jsonify({'msg': '주문 완료'})

# 주문 보여주기
@app.route("/mars", methods=["GET"])
def web_mars_get():
    # 주문 모두 가져오기
    order_list = list(db.mars.find({}, {'_id': False}))
    # orders라는 키로 order_list를 가져옴
    return jsonify({'orders': order_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
