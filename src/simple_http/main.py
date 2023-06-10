
from flask import Flask, request
 
app = Flask("src/simple_http")

@app.route('/version', methods=["GET"])
def get_version():
    res = {'status': 'ok', "version": 'v1.0.0'}
    return res

@app.route('/api/login', methods=['POST'])
def api_login():
    params = request.form if request.form else request.json
    user = params.get("user", 0)
    pwd = params.get("pwd", 0)
    if(user == 'admin' and pwd == "123456"):
        return {"status": 'ok', 'session': '12312123'}
    return {"status": 'fail', 'err': 'pwd failed!','session': '12312123'} 


@app.route('/add', methods=["GET", "POST"])
def calculate():
    if request.method == 'GET':
        params = request.args
    else:
        params = request.form if request.form else request.json
    a = params.get("a", 0)
    b = params.get("b", 0)
    c = int(a) + int(b)
    return {"result": c}


 
if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, debug=True, port=8868)