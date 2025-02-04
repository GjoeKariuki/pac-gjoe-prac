# PICTURE ARCHIVING AND COMMUNICATION SYSTEM

Based on ORTHANCTEAM/ORTHANC & OHIF Viewer

## Table of Contents

1. [Purpose](#purpose)
2. [Description](#description)
3. [Prerequisites](#prerequisites)
4. [Running](#building-and-running)
5. [Demo](#demo)
6. [Testing](#testing)

## Purpose

This is a sample setup to demonstrate how to
integrate a ORTHANC DICOM server with OHIF viewer

## Description

This demo contains:

- 2 Orthanc containers, one running the OHIF plugin and one integrating with the OHIF viewer hosted by the nginx container.
- an nginx container that:
  - exposes the Orthanc UI on http://localhost/orthanc-container/ui/app/
  - serves the OHIF viewer

## Prerequisites

- Python 3.10 or higher installed on your machine
- Docker Engine
- Web Browser (Chrome, Firefox, Brave)
- pgAdmin4 (optional)
- Postman (optional)

## Building and Running

To start the setup, type: `docker-compose up --build`

## Demo

- Orthanc UI is accessible at [http://localhost/orthanc-container/ui/app/](http://localhost/orthanc-container/ui/app/) and [http://localhost/orthanc-plugin/ui/app/](http://localhost/orthanc-plugin/ui/app/) (no login/pwd)
- upload a study in Orthanc
- click on the `OHIF viewer` button to open the viewer

## Testing

**Running Tests Locally**

1. **Start Your Docker Compose Services:**

   ```bash
   docker-compose up -d
   ```

2. **Run the Tests:**

   ```bash
    pytest ./tests/nginx-tests.py
    pytest ./tests/ohif-tests.py
    pytest ./tests/orthanc-tests.py
   ```
