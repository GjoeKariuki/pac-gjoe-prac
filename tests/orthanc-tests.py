# unit tests for the following docker services
# orthan server:

import requests

def test_orthanc_configuration():
    try:
        response = requests.get("http://localhost/orthanc-container/ui/app/#/", timeout=10)
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        # config = response.json()
        # print(f"Config response: {config}")
        # assert config['Name'] == "OHIF in container", f"Expected name 'OHIF in container', got {config['Name']}"
    except Exception as exc:
        raise AssertionError(f"Request to Orthanc timed out:, {exc}")
  



def test_ohif_viewer_integration():
    response = requests.get("http://localhost/ohif/", timeout=10)
    assert response.status_code == 200

