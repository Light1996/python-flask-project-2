from caculator import Cal
from flask import Flask


def calculator_is_instance():
    calculator = Cal(1, 2)
    assert isinstance(calculator, Cal)


def calculator_result_property():
    calc1 = Cal(1, 2)
    calc2 = Cal(3, 4)


def calculator_add_method():
    calculator = Cal(1, 1)
    assert calculator.addition() == 2


def calculator_subtract_method():
    calculator = Cal(2, 2)
    assert calculator.subtract() == 0


from app import home


def test_home():
    assert home() == "This is the check to see weather the tests are runing"


def request_index():
    app = Flask(__name__)
    client = app.test_client()
    url = "/"
    response = client.get(url)
    assert response.status_code == 202


def request_git():
    app = Flask(__name__)
    client = app.test_client()
    url = "/git"
    response = client.get(url)
    assert response.status_code == 404


def request_docker():
    app = Flask(__name__)
    client = app.test_client()
    url = "/docker"
    response = client.get(url)
    assert response.status_code == 404


def request_oop():
    app = Flask(__name__)
    client = app.test_client()
    url = "/oop"
    response = client.get(url)
    assert response.status_code == 404


def request_topic():
    app = Flask(__name__)
    client = app.test_client()
    url = "/topics"
    response = client.get(url)
    assert response.status_code == 404


def request_cicd():
    app = Flask(__name__)
    client = app.test_client()
    url = "/cicd"
    response = client.get(url)
    assert response.status_code == 404
