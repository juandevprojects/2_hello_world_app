from app.routes import HELLO_MESSAGE


def test_home_route(testing_client):
    response = testing_client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == HELLO_MESSAGE
