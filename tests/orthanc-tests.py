# unit tests for the following docker services
# orthan server:


import requests


# test orthanc/ohif configuration name
def test_orthanc_configuration():
    response = requests.get("http://localhost:8053/orthanc/health")
    assert response.status_code == 200
    config = response.json()
    assert config['Name'] == "OHIF in container"

def test_ohif_viewer_integration():
    response = requests.get("http://localhost:8053/orthanc-container/ohif/")
    assert response.status_code == 200

def test_orthanc_api():
    url = "http://localhost:8053/orthanc/instances"
    response = requests.get(url)
    assert response.status_code == 200, "Orthanc API should be accessible"

def test_orthanc_reachable():
    response = requests.get('http://localhost:8053/')
    assert response.status_code == 200

def test_dicom_web_service():
    response = requests.get('http://localhost:8053/orthanc/dicom-web/')
    assert response.status_code == 200


def test_orthanc_api_status():
    response = requests.get('http://localhost:8053/orthanc/instances')
    assert response.status_code == 200, "Orthanc API is not reachable"

def test_orthanc_status():
    url = "http://localhost:8053/orthanc"
    response = requests.get(url)
    assert response.status_code == 200, "Orthanc server is not reachable."

def test_orthanc_dicom_web_plugin():
    url = "http://localhost:8053/orthanc/dicom-web/"
    response = requests.get(url)
    assert response.status_code == 200, "DICOM Web plugin is not reachable."


def test_dicom_web_integration():
    response = requests.get('http://localhost:8042/dicom-web/instances')
    assert response.status_code == 200


def test_orthanc_rest_api():
    response = requests.get('http://localhost:8042/instances')
    assert response.status_code == 200
    assert 'DicomInstances' in response.json()


    