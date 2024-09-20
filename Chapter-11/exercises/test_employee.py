'''Write a test file for Employee with two test functions, test_give_default 
_raise() and test_give_custom_raise(). Write your tests once without using a 
fixture, and make sure they both pass. Then write a fixture so you don't have to 
create a new employee instance in each test function. Run the tests again, and 
make sure both tests still pass'''
import pytest
from EX_11_3_Employee import Employee

#Write your tests once without using a fixture, and make sure they both pass
'''
def test_give_default_raise():
    employee = Employee('Jorge', 'Macedo', 10000)
    employee.give_raise()
    assert employee.firstname=='Jorge' and employee.lastname=='Macedo' and employee.annualsalary==15000

def test_give_custom_raise():
    employee = Employee('Jorge', 'Macedo', 10000)
    employee.give_raise(7000)
    assert employee.firstname=='Jorge' and employee.lastname=='Macedo' and employee.annualsalary==17000
'''
#Then write a fixture so you don't have to create a new employee instance in each test function
@pytest.fixture
def employee_raise():
    employee_raise = Employee('Jorge', 'Macedo', 10000)
    return employee_raise


def test_give_default_raise(employee_raise):
    employee_raise.give_raise()
    assert employee_raise.firstname=='Jorge' and employee_raise.lastname=='Macedo' and employee_raise.annualsalary==15000

def test_give_custom_raise(employee_raise):
    employee_raise.give_raise(7000)
    assert employee_raise.firstname=='Jorge' and employee_raise.lastname=='Macedo' and employee_raise.annualsalary==17000