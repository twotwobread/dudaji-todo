from flask import jsonify


class Response:
    def __init__(self, status, message, data=None):
        self.status = status
        self.message = message
        self.data = data

    def to_json(self):
        return jsonify(
            dict(status=self.status, message=self.message, data=self.data)
        )
