import pytest, requests, json

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

def test_case02():
    assert(1)

def test_case03():
    assert(1)

if __name__ == '__main__':
    pytest.main(['-s', 'src/pytest1/main.py'])
    