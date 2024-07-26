# verify that the OHIF  viewer loads correctly using selenium

import requests
from selenium import webdriver



def test_ohif_reachable():
    response = requests.get('http://localhost/')
    assert response.status_code == 200

def test_ohif_configuration():
    # Check if OHIF viewer loads the custom configuration
    response = requests.get('http://localhost/ohif')
    assert response.status_code == 200

def test_ohif_viewer_selenium():
    driver = webdriver.Chrome()
    driver.get("http://localhost/ohif/")
    assert "OHIF Viewer" in driver.title, "OHIF Viewer load"
    driver.quit()

def test_ohif_viewer_configuration():
    response = requests.get("http://localhost/ohif")
    assert response.status_code == 200

# test image retrieval
def test_image_retrieval():
    response = requests.get("http://localhost/ohif/studies")
    assert response.status_code == 200


def test_ohif_viewer_load():
    response = requests.get('http://localhost/ohif/')
    assert response.status_code == 200