import json


def test_update_status_todo_ok(test_client, create_todo):
    # given
    test_client.delete("/todos")
    todo = create_todo
    todo_id = json.loads(
        test_client.post("/todos", json=todo.convert_json()).get_data()
    )["data"]["id"]
    # when
    response = test_client.patch(
        f"/todos/{todo_id}/status", json={"status": "PROGRESS"}
    )
    updated_status = json.loads(response.get_data())["data"]["status"]
    # then
    assert response.status_code == 200
    assert todo.status != updated_status


def test_update_status_todo_blank(test_client, create_todo):
    # given
    test_client.delete("/todos")
    todo = create_todo
    todo_id = json.loads(
        test_client.post("/todos", json=todo.convert_json()).get_data()
    )["data"]["id"]
    # when
    response = test_client.patch(
        f"/todos/{todo_id}/status", json={"status": ""}
    )
    # then
    assert response.status_code == 400


def test_update_status_todo_none(test_client, create_todo):
    # given
    test_client.delete("/todos")
    todo = create_todo
    todo_id = json.loads(
        test_client.post("/todos", json=todo.convert_json()).get_data()
    )["data"]["id"]
    # when
    response = test_client.patch(
        f"/todos/{todo_id}/status", json={"status": None}
    )
    # then
    assert response.status_code == 400


def test_update_status_todo_not_found(test_client):
    # given
    todo_id = 100
    # when
    response = test_client.patch(
        f"/todos/{todo_id}/status", json={"status": "PROGRESS"}
    )
    # then
    assert response.status_code == 404


def test_update_status_todo_not_exist(test_client, create_todo):
    # given
    test_client.delete("/todos")
    todo = create_todo
    todo_id = json.loads(
        test_client.post("/todos", json=todo.convert_json()).get_data()
    )["data"]["id"]
    # when
    response = test_client.patch(
        f"/todos/{todo_id}/status", json={"status": "STAGED"}
    )
    # then
    assert response.status_code == 400


def test_update_content_todo_ok(test_client, create_todo):
    # given
    test_client.delete("/todos")
    todo = create_todo
    todo_id = json.loads(
        test_client.post("/todos", json=todo.convert_json()).get_data()
    )["data"]["id"]
    # when
    response = test_client.patch(
        f"/todos/{todo_id}/content", json={"content": "new-content"}
    )
    updated_content = json.loads(response.get_data())["data"]["content"]
    # then
    assert response.status_code == 200
    assert todo.content != updated_content


def test_update_content_todo_blank(test_client, create_todo):
    # given
    test_client.delete("/todos")
    todo = create_todo
    todo_id = json.loads(
        test_client.post("/todos", json=todo.convert_json()).get_data()
    )["data"]["id"]
    # when
    response = test_client.patch(
        f"/todos/{todo_id}/content", json={"content": ""}
    )
    # then
    assert response.status_code == 400


def test_update_content_todo_none(test_client, create_todo):
    # given
    test_client.delete("/todos")
    todo = create_todo
    todo_id = json.loads(
        test_client.post("/todos", json=todo.convert_json()).get_data()
    )["data"]["id"]
    # when
    response = test_client.patch(
        f"/todos/{todo_id}/content", json={"content": None}
    )
    # then
    assert response.status_code == 400


def test_update_content_todo_not_found(test_client):
    # given
    todo_id = 100
    # when
    response = test_client.patch(
        f"/todos/{todo_id}/content", json={"content": "new-content"}
    )
    # then
    assert response.status_code == 404
