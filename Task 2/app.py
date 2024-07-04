from flask import Flask, request, jsonify, render_template
import chatbot as ct

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_query = data.get('message')

    if not user_query:
        return jsonify({"response": "Please provide a query."})

    response = ct.financial_chatbot(user_query)
    return jsonify({"response":response})

if __name__ == '__main__':
    app.run(debug=True)
