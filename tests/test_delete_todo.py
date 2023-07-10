import json


def test_delete_todo_ok(test_client, create_todo):
    # given
    test_client.delete("/todos")
    todo = create_todo
    todo_id = json.loads(
        test_client.post("/todos", json=todo.convert_json()).get_data()
    )["data"]["id"]
    # when
    response = test_client.delete(f"/todos/{todo_id}")
    # then
    assert response.status_code == 200


def test_delete_todo_not_found(test_client):
    # given
    todo_id = 100
    # when
    response = test_client.delete(f"/todos/{todo_id}")
    # then
    assert response.status_code == 404


def test_delete_all_todo_ok(test_client, create_todo):
    # given
    test_client.delete("/todos")
    test_client.post("/todos", json=create_todo.convert_json())
    # when
    response = test_client.delete("/todos")
    todo_list_length = len(
        json.loads(test_client.get("/todos").get_data())["data"]
    )
    # then
    assert response.status_code == 200
    assert todo_list_length == 0
