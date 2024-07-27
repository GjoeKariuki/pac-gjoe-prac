# test that NGINX is serving requests correctly to ORTHANC and OHIF

import requests

def test_nginx_proxy_to_orthanc():
    response = requests.get('http://localhost:8053/', timeout=10)
    assert response.status_code == 200

def test_nginx_proxy_to_ohif():
    response = requests.get('http://localhost/ohif/', timeout=10)
    assert response.status_code == 200



