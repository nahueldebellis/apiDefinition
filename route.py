from word import Word
from flask import Flask, request, jsonify
import nltk
from flask_cors import CORS
from flask import render_template as rt

app = Flask(__name__)
CORS(app)

@app.route("/words/<word>")
def synonym(word):
	w = Word()
	return w.create_response(word)
	

@app.route('/semantic/', methods=['POST'])
def semantic():
    sentence = request.data.decode("utf-8") 
    tokens = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(tokens)
    response = {}
    response['tags'] = tags
    return response

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)



