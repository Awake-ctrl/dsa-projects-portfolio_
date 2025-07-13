from flask import Flask,jsonify
import json

from graph import WeightedGraph

app=Flask(__name__)


g=WeightedGraph()



# Sample user data for demo (we'll use a JSON file later)
with open("users.json",'r') as f:
    data=json.load(f)


for record in data:
    g.add_connection(record['user1'],record['user2'],record['weight'])
    
@app.route("/")

def home():
    return "welcome to the Recommender API"

@app.route('/recommend/<username>')
def recommend(username):
    try:
        results=g.get_weighted_suggestions(username)
        return jsonify({
            "user":username,
            "recommendations":results
        })
        
    except Exception as e:
        return jsonify({
            "error":str(e)
        }),400
        

if __name__=='__main__':
    app.run(debug=True)