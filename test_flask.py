
import pytest
from app import app, allowed_file


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_allowed_file():
    allowed_filename = 'test.png'
    new_file = 'test.jpeg'
    file = 'test.jpg'
    expected = True
    actual = allowed_file(allowed_filename)
    actual_new_file = allowed_file(new_file)
    actual_file = allowed_file(file)
    assert expected == actual
    assert expected == actual_new_file
    assert expected == actual_file


def test_upload_file(client):
    with open('gory.jpeg', 'rb') as f:
        filename = f.name
        print(filename)
        filename = allowed_file(filename)
        post_return = client.post(
            path='/upload', data={'file': f}
        )
        print(post_return)
        assert post_return.status_code == 200
    with open('file.txt', 'r') as f:
        filename = f.name
        print(filename)
        filename = allowed_file(filename)
        post_return = client.post(
            path='/upload', data={'file': f}
        )
        print(post_return.data)
        response = post_return.data.decode('utf-8')
        assert post_return.status_code == 422
        assert 'Picture format is not correct' in response


def test_root(client):
    post_return = client.post(
        path='/upload', data={'file': 'test.jpeg'}
    )
    print(post_return)
    response = post_return.data.decode('utf-8')
    assert post_return.status_code == 422
    assert 'No file part' in response
