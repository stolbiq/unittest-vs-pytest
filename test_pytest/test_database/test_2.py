import pytest


def test_data_base_save():
    print('######## running save')

def test_data_base_delete():
    print('######## running delete')

@pytest.mark.non_database
def test_non_data_base():
    print('######## non database test')