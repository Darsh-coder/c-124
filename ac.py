
from flask import Flask,jsonify,request
app = Flask(__name__)

tasks = [

{
    "id":1,
    "name":"jhon loke",
    "contact":"3216547890",
    "status":False

},
{
    "id":2,
    "name":"ton loke",
    "contact":"3652147890",
    "status":False

}

]

@app.route("/hello")
def hello_world():
    return "hello world"


@app.route("/get-data")
def get_task():
    return jsonify({ 
        "data":tasks
    })
@app.route("/add-data",methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"pls provide the data"
        },400)
    task = {
        
    "id":tasks[-1]["id"]+1,
    "name":request.json["name"],
    "contact":request.json.get("contact",""),
    "status":False
    }
    tasks.append(task)
    return jsonify({
            "status":"sucess",
            "message":"task added sucessfully"
        },400)

if (__name__ == "__main__"):
    app.run(debug = True)




