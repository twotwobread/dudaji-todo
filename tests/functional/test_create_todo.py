def test_create_todo_ok(test_client):
    test_client.delete("/todos")
    content = "content"
    response = test_client.post("/todos", json={"content": content})
    assert response.status_code == 200
    assert bytes(content, "utf-8") in response.data


def test_create_todo_bad_request_by_content_blank(test_client):
    test_client.delete("/todos")
    content = ""
    response = test_client.post("/todos", json={"content": content})
    assert response.status_code == 400


def test_create_todo_bad_request_by_content_none(test_client):
    test_client.delete("/todos")
    content = None
    response = test_client.post("/todos", json={"content": content})
    assert response.status_code == 400
