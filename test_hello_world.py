from hello_world import build_hello_world


def test_hello_world():
    assert build_hello_world() == "Hello, world!"
