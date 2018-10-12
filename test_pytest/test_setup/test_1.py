import pytest
from setup_classes import Session

@pytest.fixture
def session():
    session = Session()
    yield session
    session.close()

def test_db_save(session):
    """Test db save"""
    print('######## running save')

def test_db_delete(session):
    """Test db deletion"""
    print('######## running delete')

def test_non_db():
    print('######## non db test')