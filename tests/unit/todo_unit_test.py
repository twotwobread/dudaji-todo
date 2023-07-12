from app.service import todo_service


def test_get(create_todo):
    # given
    todo = create_todo
    todo_service.todo_repository.insert(todo)
    # when
    find_todo = todo_service.get_todo(todo.id)
    # then
    assert todo.id == find_todo.id


def test_get_all(create_todo_list):
    # given
    todo_service.todo_repository.clear()
    insert_todos = create_todo_list
    insert_todo_list(todo_service.todo_repository, insert_todos)
    # when
    find_todos = todo_service.get_all_todo()
    # then
    assert len(insert_todos) == len(find_todos)


def test_update_status(create_todo):
    # given
    status = "PROGRESS"
    todo_service.todo_repository.clear()
    todo = create_todo
    todo_service.todo_repository.insert(todo)
    # when
    todo.status = status
    updated_todo = todo_service.update_todo_status(todo.to_json(), todo.id)
    # then
    assert status == updated_todo.status


def test_update_content(create_todo):
    # given
    content = "update content"
    todo_service.todo_repository.clear()
    todo = create_todo
    todo_service.todo_repository.insert(todo)
    # when
    todo.content = content
    updated_todo = todo_service.update_todo_status(todo.to_json(), todo.id)
    # then
    assert content == updated_todo.content


def insert_todo_list(repository, todo_list):
    for todo in todo_list:
        repository.insert(todo)
