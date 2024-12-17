'''7-3. Testing python_repos.py: In python_repos.py, we printed the value of 
status_code to make sure the API call was successful. Write a program called 
test_python_repos.py that uses pytest to assert that the value of status_code 
is 200. Figure out some other assertions you can make: for example, that the 
number of items returned is expected and that the total number of repositories is 
greater than a certain amount.'''
from python_repos import check_url
import requests

#make an api call and check the response
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

#Função para verificar o status code.
def test_check_url_status_code():
    result = check_url(url)
    assert result.status_code == 200
#função para verificar se a quantidade de items é maior que 30
def test_number_items():
    result = check_url(url)
    r = result.json()
    assert len(r['items']) >= 30