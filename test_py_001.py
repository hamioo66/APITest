# -*- coding：utf-8 -*-
import pytest
import requests
@pytest.mark.skip(reason='忽略执行该测试用例')
def test_001():
    assert 1==1

@pytest.mark.login
def test_login_001():
    assert 2==3
@pytest.mark.login
def test_logout_002():
    pass
def test_get_page_baidu(url='http://www.baidu.com/'):
    r = requests.get(url=url)
    assert r.status_code==200
def test_get_page_taobao(url='http://www.taobao.com/'):
    r = requests.get(url=url)
    assert r.status_code==200
def test_get_page_qq(url='http://www.qq.com/'):
    r = requests.get(url=url)
    assert r.status_code==200
