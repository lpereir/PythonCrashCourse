import requests

#make an api call and check the response
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

def check_url(url):
    headers = {"Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)
    print(f"Status code: {r.status_code}")
    #Convert the responde object to a dictionary
    return r

response = check_url(url)
response_dict = response.json()

print(f'Total repositories: {response_dict['total_count']}')
print(f'Complete results: {not response_dict['incomplete_results']}')
#Explore information about the repositories.
repo_dicts = response_dict['items']
print(f'Repositories returned: {len(repo_dicts)}')

#examine the first repository
print('\nSelected information about the first repository:')
for repo_dict in repo_dicts:
    print(f'Name: {repo_dict['name']}')
    print(f'Owner: {repo_dict['owner']['login']}')
    print(f'Stars: {repo_dict['stargazers_count']}')
    print(f'Repository: {repo_dict['html_url']}')
    print(f'Created: {repo_dict['created_at']}')
    print(f'Updated: {repo_dict['updated_at']}')
    print(f'Description: {repo_dict['description']}')