from flask import Flask, request, jsonify, render_template
from preprocess_data import Question

# 初始化Question类
question_handler = Question()
app = Flask(__name__)

# 路由和视图函数
@app.route('/')
def home():
    return render_template('app.html')

@app.route('/query', methods=['POST'])
def query():
    user_input = request.json['query']
    print(user_input)
    outputText = question_handler.question_process(user_input)
    print(outputText)
    response = {'result': outputText}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True,port=5000)
