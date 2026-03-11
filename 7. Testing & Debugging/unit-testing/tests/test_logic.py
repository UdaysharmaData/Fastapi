import pytest
from app.logic import is_elegible_for_loan


def test_eligible_user():
    assert is_elegible_for_loan(60000,25,'employed') == True  

def test_underage_user():
    assert is_elegible_for_loan(60000,18,'employed') == False

def test_low_income():
    assert is_elegible_for_loan(10000,25,'employed') == False

def test_employe_status():
    assert is_elegible_for_loan(60000,25,'unemploy') == False

def test_boundary_case():
    assert is_elegible_for_loan(50000,21,'employed') == True