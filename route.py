from word import Word
from flask import Flask, request, jsonify, send_file
import nltk
from flask_cors import CORS
import pdfkit
import os
import  subprocess
from flask import render_template as rt

app = Flask(__name__)
CORS(app)

@app.route("/words/<word>")
def synonym(word):
	w = Word()
	return w.create_response(word)
	

@app.route('/pdf/<text>')
def pdf(text):
    sentence = text
    WKHTMLTOPDF_CMD = subprocess.Popen(['which', os.environ.get('WKHTMLTOPDF_BINARY', 'wkhtmltopdf')], stdout=subprocess.PIPE).communicate()[0].strip()
    return pdfkit.from_string(sentence, configuration=configuration)
    #pdfkit.from_string(sentence, 'out.pdf')
    #return send_file('./out.pdf', mimetype='application/pdf')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)



