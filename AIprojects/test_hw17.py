import sqlite_lib as sb
import pytest

@pytest.fixture
def before_after_operations_db():
    # BEFORE
    sb.connect('E-commerce Customer Behavior - Sheet1.db')

    yield  # test_get_years

    # AFTER
    sb.close()

def members_count(mb_type: str):
    sb.connect('E-commerce Customer Behavior - Sheet1.db')
    temp = sb.run_query_select(f'select count(*) from e_commerce where "Membership Type" = "{mb_type}"')[0][0]
    sb.close()
    return temp

def test_gold(before_after_operations_db):
    assert members_count('Gold') == 117

def test_silver(before_after_operations_db):
    assert members_count('Silver') == 117

def test_bronze(before_after_operations_db):
    assert members_count('Bronze') == 116