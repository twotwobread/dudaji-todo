import pytest
import os
from app import create_app
from app.model.todo import Todo
from app.model.status import Status


@pytest.fixture(scope="module")
def test_client():
    os.environ["CONFIG_TYPE"] = "config.TestingConfig"
    flask_app = create_app()

    # 테스트를 위해 구성된 플라스트 애플리케이션을 사용하는 테스트 클라이언트 생성
    with flask_app.test_client() as testing_client:
        # 애플리케이션 컨텍스트를 생성.
        with flask_app.app_context():
            yield testing_client  # 테스트가 발생하고 수행되는 위치.


@pytest.fixture(scope="module")
def create_todo():
    todo = Todo(status=Status.YET, content="content")
    return todo
