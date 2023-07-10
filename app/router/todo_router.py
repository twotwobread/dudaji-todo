from flask import Blueprint, request, jsonify
from app.model.todo import Todo
from app.model.status import STATUS
from app.model.response import Response
from app.model.http_status import HTTP_STATUS

bp = Blueprint("todo", __name__, url_prefix="/todos")
DB = {}


@bp.route("", methods=("POST",))
def create_todo():
    request_data = request.get_json()
    if not request_data or len(request_data["content"]) <= 0:
        return (
            jsonify(
                Response(
                    HTTP_STATUS.BAD_REQUEST,
                    "Impossible blank content or null content",
                ).covert_json(),
            ),
            HTTP_STATUS.BAD_REQUEST,
        )

    new_todo = Todo(status=STATUS.YET, content=request_data["content"])
    DB[new_todo.id] = new_todo
    return jsonify(
        Response(
            HTTP_STATUS.OK, "Create Todo Success", new_todo.convert_json()
        ).covert_json(),
    )


@bp.route("/<int:todo_id>", methods=("GET",))
def get_todo(todo_id):
    if not todo_id in DB:
        return (
            jsonify(
                Response(
                    HTTP_STATUS.NOT_FOUND, f"Not Found todo-id: {todo_id}"
                ).covert_json(),
            ),
            HTTP_STATUS.NOT_FOUND,
        )
    return jsonify(
        Response(
            HTTP_STATUS.OK, "Read Todo Success", DB[todo_id].convert_json()
        ).covert_json()
    )


@bp.route("", methods=("GET",))
def get_all_todo():
    all_todo_list = list(map(lambda x: DB[x].convert_json(), DB.keys()))
    return jsonify(
        Response(
            HTTP_STATUS.OK, "Read All Todo Success", all_todo_list
        ).covert_json()
    )


@bp.route("/<int:todo_id>", methods=("DELETE",))
def delete_todo(todo_id):
    if not todo_id in DB:
        return (
            jsonify(
                Response(
                    HTTP_STATUS.NOT_FOUND, f"Not Found todo-id: {todo_id}"
                ).covert_json(),
            ),
            HTTP_STATUS.NOT_FOUND,
        )
    del DB[todo_id]
    return jsonify(
        Response(HTTP_STATUS.OK, "Delete Todo Success").covert_json(),
    )
