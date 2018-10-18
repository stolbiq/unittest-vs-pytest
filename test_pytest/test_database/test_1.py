import pytest
from database_classes import Session, Connection

@pytest.fixture
def session():
    session = Session()
    yield session
    session.close()

def test_data_base_save(session):
    print('######## running save')

def test_data_base_delete(session):
    print('######## running delete')

def test_non_data_base():
    print('######## non database test')
