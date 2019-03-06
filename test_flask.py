
import pytest
from app import app, allowed_file


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_allowed_file():
    allowed_filename = 'test.png'
    expected = True
    actual = allowed_file(allowed_filename)
    assert expected == actual


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


def test_root(client):
    post_return = client.post(
        path='/upload', data={'file': 'test.jpeg'}
    )
    print(post_return)
    assert post_return.status_code == 422

        # with open('file.txt', 'r') as f:
        #     filename = f.name
        #     print(filename)
        #     filename = allowed_file(filename)
        #     post_return = client.post(
        #         path='/upload', data={'file': f}
        #     )
        #     print(post_return)
        #     assert post_return.status_code == 422


# def test_post_tinyjpg(client):
#  post_return = client.get('/upload', data={'file': 'gory.jpeg'}, follow_redirects=True)
#     print(post_return)
#     assert post_return.status_code ==  200


# def test_root():
# assert False
