import requests
import pprint
import pytest
import allure
import time


@allure.feature('Check ccy')
@allure.severity('Blocker')
@allure.issue('jira link')
@allure.testcase('https://testrail.ru')
@pytest.mark.parametrize('ccy', ['USD', 'EUR', 'BTC', 'RUB'])
def test_check_ccy(ccy):
    r = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
    print(r.json())
    item = r.json()
    sale = [x.get("sale") for x in item if x.get('ccy') == ccy]
    sale = str(sale)
    sale = sale[2: -4]
    sale = float(sale)
    assert sale > 0

@allure.feature('Check ccy')
@allure.severity('Blocker')
@allure.issue('jira link')
@allure.testcase('https://testrail.ru')
def test_req1():
    r = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
    time.sleep(10)
    assert r.status_code == 200

@allure.feature('Check ccy')
@allure.severity('Blocker')
@allure.issue('jira link')
@allure.testcase('https://testrail.ru')
def test_req2():
    r = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
    print(r.headers)
    assert 'application/json' in r.headers['Content-Type']

@allure.feature('Check test input')
@allure.severity('Blocker')
@allure.issue('jira link')
@allure.testcase('https://testrail.ru')
@pytest.mark.parametrize('test_input', [1,2,3])
def test_parametrize_with_mark_single(test_input):
    assert test_input==3

@allure.feature('test feature 1 ')
@allure.severity('Major')
@allure.issue('jira link')
@allure.testcase('https://testrail.ru')
#параметризация нескольких параметров
@pytest.mark.parametrize("test_input, expected", [("3+5",  8), ('6+9', 15), ('5*5', 30)],
                         ids= ['Three plus five', 'six plus nine', 'five by five'])
def test_parametrize_with_multiply_mark(test_input, expected):
    assert eval(test_input) == expected

@allure.feature('test feature')
@allure.severity('Minor')
@allure.issue('jira link3')
@allure.testcase('https://testrail.ru/3')
#Вложенная параметризация
@pytest.mark.parametrize('x', [0,1])
@pytest.mark.parametrize('y', [2,3])
def test_foo(x,y):
    assert  x == y

def test_skip():
    pytest.skip('reasond for skip')



# NEW FEATURE
@allure.feature('test feature 1 ')
@allure.severity('Major')
@allure.issue('jira link')
@allure.testcase('https://testrail.ru')
#параметризация нескольких параметров
@pytest.mark.parametrize("test_input, expected", [("3+5",  8), ('6+9', 15), ('5*5', 30)],
                         ids= ['Three plus five', 'six plus nine', 'five by five'])
def test_parametrize_with_multiply_mark(test_input, expected):
    assert eval(test_input) == expected




















