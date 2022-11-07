import pytest
from api import get_app

def test_home_page_post():

    flask_app = get_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/greeting')
        assert response.status_code == 200
        