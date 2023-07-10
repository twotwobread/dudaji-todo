from flask import Blueprint, request, jsonify
from app.model.todo import Todo
from app.model.status import Status
from app.model.response import Response
from app.model.http_status import HttpStatus

bp = Blueprint("todo", __name__, url_prefix="/todos")
DB = {}


@bp.route("", methods=("POST",))
def create_todo():
    request_data = request.get_json()
    if not request_data.get("content"):
        return (
            jsonify(
                Response(
                    HttpStatus.BAD_REQUEST,
                    "Impossible blank content or null content",
                ).covert_json(),
            ),
            HttpStatus.BAD_REQUEST,
        )

    new_todo = Todo(status=Status.YET, content=request_data["content"])
    DB[new_todo.id] = new_todo
    return jsonify(
        Response(
            HttpStatus.OK, "Create Todo Success", new_todo.convert_json()
        ).covert_json(),
    )


@bp.route("/<int:todo_id>", methods=("GET",))
def get_todo(todo_id):
    if not todo_id in DB:
        return (
            jsonify(
                Response(
                    HttpStatus.NOT_FOUND, f"Not Found todo-id: {todo_id}"
                ).covert_json(),
            ),
            HttpStatus.NOT_FOUND,
        )
    return jsonify(
        Response(
            HttpStatus.OK, "Read Todo Success", DB[todo_id].convert_json()
        ).covert_json()
    )


@bp.route("", methods=("GET",))
def get_all_todo():
    all_todo_list = list(map(lambda x: DB[x].convert_json(), DB.keys()))
    return jsonify(
        Response(
            HttpStatus.OK, "Read All Todo Success", all_todo_list
        ).covert_json()
    )


@bp.route("/<int:todo_id>", methods=("DELETE",))
def delete_todo(todo_id):
    if not todo_id in DB:
        return (
            jsonify(
                Response(
                    HttpStatus.NOT_FOUND, f"Not Found todo-id: {todo_id}"
                ).covert_json(),
            ),
            HttpStatus.NOT_FOUND,
        )
    del DB[todo_id]
    return jsonify(
        Response(HttpStatus.OK, "Delete Todo Success").covert_json(),
    )


@bp.route("", methods=("DELETE",))
def clear_all_todo():
    DB.clear()
    return jsonify(
        Response(HttpStatus.OK, "Clear All Todo Success").covert_json(),
    )


@bp.route("/<int:todo_id>/status", methods=("PATCH",))
def update_todo_status(todo_id):
    request_data = request.get_json()
    if not request_data.get("status"):
        return (
            jsonify(
                Response(
                    HttpStatus.BAD_REQUEST,
                    "Impossible blank status or null status",
                ).covert_json(),
            ),
            HttpStatus.BAD_REQUEST,
        )

    update_status = request_data["status"]
    if not todo_id in DB:
        return (
            jsonify(
                Response(
                    HttpStatus.NOT_FOUND, f"Not Found todo-id: {todo_id}"
                ).covert_json(),
            ),
            HttpStatus.NOT_FOUND,
        )
    if not update_status in Status.__members__:
        return (
            jsonify(
                Response(
                    HttpStatus.BAD_REQUEST, f"Not exist status: {update_status}"
                ).covert_json(),
            ),
            HttpStatus.BAD_REQUEST,
        )
    update_todo = DB[todo_id]
    update_todo.status = Status[update_status]
    return jsonify(
        Response(
            HttpStatus.OK,
            "Update Todo Status Success",
            update_todo.convert_json(),
        ).covert_json()
    )


@bp.route("/<int:todo_id>/content", methods=("PATCH",))
def update_todo_content(todo_id):
    request_data = request.get_json()
    if not request_data.get("content"):
        return (
            jsonify(
                Response(
                    HttpStatus.BAD_REQUEST,
                    "Impossible blank content or null content",
                ).covert_json(),
            ),
            HttpStatus.BAD_REQUEST,
        )

    if not todo_id in DB:
        return (
            jsonify(
                Response(
                    HttpStatus.NOT_FOUND, f"Not Found todo-id: {todo_id}"
                ).covert_json(),
            ),
            HttpStatus.NOT_FOUND,
        )

    update_todo = DB[todo_id]
    update_todo.content = request_data["content"]
    return jsonify(
        Response(
            HttpStatus.OK,
            "Update Todo Content Success",
            update_todo.convert_json(),
        ).covert_json()
    )
