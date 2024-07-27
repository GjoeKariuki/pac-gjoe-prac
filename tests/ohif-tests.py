# verify that the OHIF  viewer loads correctly using selenium

import requests
from selenium import webdriver



def test_ohif_reachable():
    # Check if OHIF viewer deployment successful
    response = requests.get('http://localhost/ohif/', timeout=10)
    assert response.status_code == 200

def test_ohif_viewer_selenium():
    # check if ohif is browser accesssible
    driver = webdriver.Chrome()
    driver.get("http://localhost/ohif/")
    assert "OHIF Viewer" in driver.title, "OHIF Viewer load"
    driver.quit()



# test image retrieval
def test_image_retrieval():
    response = requests.get("http://localhost/ohif/studies", timeout=20)
    assert response.status_code == 200


