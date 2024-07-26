# test that NGINX is serving requests correctly to ORTHANC and OHIF

import requests




def test_nginx_proxy():
    response  = requests.get("http://localhost/")
    assert response.status_code == 200, "Nginx proxy"


def test_nginx_proxy_to_orthanc():
    response = requests.get('http://localhost/orthanc')
    assert response.status_code == 200

def test_nginx_proxy_to_ohif():
    response = requests.get('http://localhost/ohif')
    assert response.status_code == 200

def test_nginx_proxy_ver():
    response = requests.get('http://localhost/')
    assert response.status_code == 200
    assert 'Orthanc' in response.text or 'OHIF' in response.text


