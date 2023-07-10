import json


def test_read_todo_ok(test_client, create_todo):
    # given
    test_client.delete("/todos")
    todo = create_todo
    todo_id = json.loads(
        test_client.post("/todos", json=todo.convert_json()).get_data()
    )["data"]["id"]
    # when
    response = test_client.get(f"/todos/{todo_id}")
    # then
    assert 200 == response.status_code
    assert todo_id == json.loads(response.get_data())["data"]["id"]


def test_read_todo_not_found(test_client):
    # given
    test_client.delete("/todos")
    # when
    todo_id = 1000
    response = test_client.get(f"/todos/{todo_id}")
    # then
    assert 404 == response.status_code


def test_read_all_todo_ok(test_client, create_todo):
    # given
    test_client.delete("/todos")
    loop = 10
    todo_list = create_todo_loop(loop, create_todo)
    for todo in todo_list:
        test_client.post("/todos", json=todo.convert_json())
    # when
    response = test_client.get("/todos")
    # then
    assert 200 == response.status_code
    assert loop == len(json.loads(response.get_data())["data"])


def create_todo_loop(loop, create_todo):
    return [create_todo for _ in range(loop)]
