from src.presentation.controllers.user_register_controller import UserRegisterController
from src.data.tests.user_register import UserRegisterSpy
from src.presentation.http_types.http_response import HttpResponse

class HttpRequestMock:
    def __init__(self) -> None:
        self.body = { "first_name": "first_name_test", "last_name": "last_name_test", "age": 12 }

def test_handle():
    http_request = HttpRequestMock()
    use_case = UserRegisterSpy()
    user_finder_controller = UserRegisterController(use_case)

    response = user_finder_controller.handle(http_request)

    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"] is not None