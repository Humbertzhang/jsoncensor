from flask import Flask
from flask import request, jsonify
from jsoncensor import JsonCensor

app = Flask(__name__)

@app.route("/test/", methods = ['POST'])
def perfect():
    if request.method == 'POST':
        # Start Check
        standard = {
            "username":"", 
            "password":"", 
            "email":""
        }
        jc = JsonCensor(standard, request.get_json())
        result = jc.check()
        if result['statu'] is not True:
            return jsonify({"JSON_msg":result})
        # End Check

        # Your Code Here

        return jsonify({"msg":"ok"})

if __name__ == '__main__':
    app.run()
