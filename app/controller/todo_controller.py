from flask import Blueprint, request
from app.common.response import Response
from app.common.http_status import HttpStatus
from app.service import todo_service

bp = Blueprint("todo", __name__, url_prefix="/todos")


@bp.post("")
def create_todo():
    new_todo = todo_service.create(request.get_json())
    response = Response(
        HttpStatus.OK, "Create Todo Success", new_todo.to_json()
    )
    return response.to_json(), response.status


@bp.get("/<int:todo_id>")
def get_todo(todo_id):
    todo = todo_service.get_todo(todo_id)
    response = Response(HttpStatus.OK, "Read Todo Success", todo.to_json())
    return response.to_json(), response.status


@bp.get("")
def get_all_todo():
    all_todo_list = todo_service.get_all_todo()
    response = Response(
        HttpStatus.OK,
        "Read All Todo Success",
        list(map(lambda x: x.to_json(), all_todo_list)),
    )
    return response.to_json(), response.status


@bp.delete("/<int:todo_id>")
def delete_todo(todo_id):
    todo_service.delete_todo(todo_id)
    response = Response(HttpStatus.OK, "Delete Todo Success")
    return response.to_json(), response.status


@bp.delete("")
def clear_all_todo():
    todo_service.clear_todo()
    response = Response(HttpStatus.OK, "Clear All Todo Success")
    return response.to_json(), response.status


@bp.patch("/<int:todo_id>/status")
def update_todo_status(todo_id):
    update_todo = todo_service.update_todo_status(request.get_json(), todo_id)
    response = Response(
        HttpStatus.OK, "Update Todo Status Success", update_todo.to_json()
    )
    return response.to_json(), response.status


@bp.patch("/<int:todo_id>/content")
def update_todo_content(todo_id):
    update_todo = todo_service.update_todo_content(request.get_json(), todo_id)
    response = Response(
        HttpStatus.OK, "Update Todo Content Success", update_todo.to_json()
    )
    return response.to_json(), response.status
