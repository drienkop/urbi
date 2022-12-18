# Urbi

Urbi is the easiest way to create simulated API services, inspired by [WireMock](https://wiremock.org/) and built on [Flask](https://flask.palletsprojects.com/en/2.2.x).

<ins>It is not recommended to use the stub API in a production environment; it should only be utilized for testing purposes, such as integration tests.</ins>

## Running your stubbed API Service with Docker

To run your stubbed API service using Urbi, define a mapping file (request-reponse) in the form of a Flask [blueprint](https://flask.palletsprojects.com/en/2.2.x/blueprints/). 

### Example mapping

```python
from flask import Blueprint

blueprint = Blueprint("hello", __name__)


@blueprint.route("/hello")
def hello():
    return {"Hello": "World"}
```
 Store the mapping file in a dedicated mappings folder.

After that include the `urbi` container in your `docker-compose.yaml` with a volume which maps your mappings folder and point it to the `/mappings` folder in the container:

### Example docker-compose.yaml
```
services:
  urbi:
    image: drienkop/urbi:latest
    volumes:
      - ./mappings:/mappings 
```

### Run the stubbed API service

Simply run:

`docker-compose up`

Which will start the webserver with your stubbed API service:
```bash
$ docker-compose up
Starting urbi_urbi_1 ... done
Attaching to urbi_urbi_1
urbi_1  |  * Debug mode: off
urbi_1  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
urbi_1  |  * Running on all addresses (0.0.0.0)
```

Try your new stubbed API service by calling the endpoint:

```bash
$ curl -i http://localhost:5000/hello
HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.11.1
Date: Sun, 18 Dec 2022 15:59:39 GMT
Content-Type: application/json
Content-Length: 18
Connection: close

{"Hello":"World"}
```
