from flask import Flask, request, jsonify, make_response, render_template, session
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://enel:TQgBCNu8IimXt1QL@cluster0.enrjm60.mongodb.net/?retryWrites=true&w=majority")
db = client.sample_mflix
moviesCollection = db.movies

@app.route('/', methods=['GET'])
def home():
    data = moviesCollection.find().limit(40)
    return render_template('index.html', data = data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)