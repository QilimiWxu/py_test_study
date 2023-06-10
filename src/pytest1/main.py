import pytest, requests, json
import os

host = '127.0.0.1:8868'

def test_case01():
    try:
        url = 'http://' + host + '/version'
        res = requests.get(url)
        print(url)
        if(res == None):
            assert(0)
        if(res.status_code != 200):
            assert(0)
        if(res.content == None or len(res.content) == 0):
            assert(0)
        res_param = json.loads(res.text)
        if('status' in res_param.keys() and 'version' in res_param.keys()):
            if(res_param['status'] == 'ok' and res_param['version'] == 'v1.0.0'):
                return
    except Exception as e1:
        print(e1)
    assert(0)

def test_login_user():
    try:
        url = 'http://' + host + '/api/login'
        param = {
            'user':'admin',
            'pwd':'123456'
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
        res = requests.post(url, param, headers=headers)
        print(url)
        if(res == None):
            assert(0)
        if(res.status_code != 200):
            assert(0)
        if(res.content == None or len(res.content) == 0):
            assert(0)
        res_param = json.loads(res.text)
        if('status' in res_param.keys()and 'session' in res_param.keys()):
            if(res_param['status'] == 'ok'and len(res_param['session']) > 1):
                return
    except Exception as e1:
        print(e1)
    assert(0)

def test_case03():
    assert(1)

if __name__ == '__main__':
    if(os.path.exists('src/pytest1/main.py')):
        pytest.main(['-s', 'src/pytest1/main.py'])
    elif(os.path.exists('main.py')):
        pytest.main(['-s', 'main.py'])
    