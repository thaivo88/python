Your program will use a web <i>application programming interface (API)</i> to automatically request specific information from a website—rather than entire pages—and then use that information to generate a visualization. Because programs written like this will always use current data to generate a visualization, even when that data might be rapidly changing, it will always be up to date.

                                                              Web API:

A web API is a part of a website designed to interact with programs. Those programs use very specific URLs to request certain information. This kind of request is called an API <i>call</i>. The requested data will be returned in an easily processed format, such as JSON or CSV.



Git and GitHub:

GitHub (https://github.com/) takes its name from Git, a distributed version control system. Git helps people manage their work on a project, so changes made by one person won’t interfere with changes other people are making. When you implement a new feature in a project, Git tracks the changes you make to each file. When your new code works, you <i>commit</i> the changes you’ve made, and Git records the new state of your project. If you make a mistake and want to revert your changes, you can easily return to any previously working state.
Projects on GitHub are stored in repositories, which contain everything associated with the project: its code, information on its collaborators, any issues or bug reports, and so on.




Processing an API Response
```
import requests
# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
# Store API response in a variable.
response_dict = r.json()
# Process results.
print(response_dict.keys())
--------------- Output ---------------
Status code: 200
dict_keys(['total_count', 'incomplete_results', 'items'])
```

GitHub is currently on the third version of its API, so we define headers for the API call w that ask explicitly to use this version of the API.
Then we use <i>requests</i> to make the call to the API
We call <i>get()</i> and pass it the URL and the header that we defined, and we assign the response object to the variable <i>r</i>.
The response object has an attribute called <i>status_code</i>, which tells us whether the request was successful. (A status code of 200 indicates a successful response.)
The API returns the information in JSON format, so we use the <i>json()</i> method to convert the information to a Python dictionary. We store the resulting dictionary in <i>response_dict</i>.

  
Working with the response dictionary
With the information from the API call stored as a dictionary, we can work with the data stored there.
```
import requests
# Make an API call and store the response.
--snip--
# Store API response in a variable.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")
# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")
# Examine the first repository.
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
  print(key)
--------------- Output ---------------  
Status code: 200
Total repositories: 3494030
Repositories returned: 30

Keys: 73
archive_url
archived
assignees_url
--snip--
url
watchers
watchers_count  
```

Let’s pull out the values for some of the keys in repo_dict:
```
--snip--
# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")
# Examine the first repository.
repo_dict = repo_dicts[0]
print("\nSelected information about first repository:")
print(f"Name: {repo_dict['name']}")
print(f"Owner: {repo_dict['owner']['login']}")
print(f"Stars: {repo_dict['stargazers_count']}")
print(f"Repository: {repo_dict['html_url']}")
print(f"Created: {repo_dict['created_at']}")
print(f"Updated: {repo_dict['updated_at']}")
print(f"Description: {repo_dict['description']}")
--------------- Output ---------------  
Status code: 200
Total repositories: 3494032
Repositories returned: 30
Selected information about first repository:
Name: awesome-python
Owner: vinta
Stars: 61549
Repository: https://github.com/vinta/awesome-python
Created: 2014-06-27T21:00:06Z
Updated: 2019-02-17T04:30:00Z
Description: A curated list of awesome Python frameworks, libraries, software and resources
```


Summarizing the top repositories
When we make a visualization for this data, we’ll want to include more than one repository. Let’s write a loop to print selected information about each repository the API call returns so we can include them all in the visualization.
```
--snip--
# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
  print(f"\nName: {repo_dict['name']}")
  print(f"Owner: {repo_dict['owner']['login']}")
  print(f"Stars: {repo_dict['stargazers_count']}")
  print(f"Repository: {repo_dict['html_url']}")
  print(f"Description: {repo_dict['description']}")
--------------- Output --------------- 
Status code: 200
Total repositories: 3494040
Repositories returned: 30
Selected information about each repository:
Name: awesome-python
Owner: vinta
Stars: 61549
Repository: https://github.com/vinta/awesome-python
Description: A curated list of awesome Python frameworks, libraries, software
and resources
Name: system-design-primer
Owner: donnemartin
Stars: 57256
Repository: https://github.com/donnemartin/system-design-primer
Description: Learn how to design large-scale systems. Prep for the system
design interview. Includes Anki flashcards.
--snip--
Name: python-patterns
Owner: faif
Stars: 19058
Repository: https://github.com/faif/python-patterns
Description: A collection of design patterns/idioms in Python
```


Monitoring API rate limits
Most APIs are rate limited, which means there’s a limit to how many requests you can make in a certain amount of time. To see if you’re approaching GitHub’s limits, enter https://api.github.com/rate_limit into a web browser. You should see a response that begins like this:
```
{
  "resources": {
    "core": {
      "limit": 60,
      "remaining": 58,
      "reset": 1550385312
    },
    "search": {
      "limit": 10,
      "remaining": 8,
      "reset": 1550381772
    },
--snip--
```
We see at that the limit is 10 requests per minute and that we have 8 requests remaining for the current minute. The reset value represents the time in Unix or epoch time (the number of seconds since midnight on January 1, 1970) when our quota will reset. If you reach your quota, you’ll get a short response that lets you know you’ve reached the API limit. If you reach the limit, just wait until your quota resets.






                                          Visualizing Repositories Using Plotly
                                          
```
import requests
from plotly.graph_objs import Bar
from plotly import offline
# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
# Process results.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars = [], []
for repo_dict in repo_dicts:
  repo_names.append(repo_dict['name'])
  stars.append(repo_dict['stargazers_count'])
# Make visualization.
data = [{
  'type': 'bar',
  'x': repo_names,
  'y': stars,
}]
my_layout = {
  'title': 'Most-Starred Python Projects on GitHub',
  'xaxis': {'title': 'Repository'},
  'yaxis': {'title': 'Stars'},
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
```
--------------- Output --------------- 
![image](https://user-images.githubusercontent.com/15881158/156674066-93b2532d-863a-4954-a0ca-3d08cf8f73e5.png)



Adding Custom Tooltips
In Plotly, you can hover the cursor over an individual bar to show the information that the bar represents. This is commonly called a <i>tooltip</i>, and in this case, it currently shows the number of stars a project has.
```
--snip--
# Process results.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars, labels = [], [], []
for repo_dict in repo_dicts:
  repo_names.append(repo_dict['name'])
  stars.append(repo_dict['stargazers_count'])
  owner = repo_dict['owner']['login']
  description = repo_dict['description']
  label = f"{owner}<br />{description}"
  labels.append(label)
# Make visualization.
data = [{
  'type': 'bar',
  'x': repo_names,
  'y': stars,
  'hovertext': labels,
  'marker': {
    'color': 'rgb(60, 100, 150)',
    'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
  },
  'opacity': 0.6,
}]
--snip--
```
Plotly allows you to use HTML code within text elements, so we generate a string for the label with a line break (<br/>) between the project owner’s username and the description.


Adding clickable links to our graph
```
--snip--
# Process results.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
  repo_name = repo_dict['name']
  repo_url = repo_dict['html_url']
  repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
  repo_links.append(repo_link)
  stars.append(repo_dict['stargazers_count'])
  --snip--
# Make visualization.
data = [{
  'type': 'bar',
  'x': repo_links,
  'y': stars,
  --snip--
}]
--snip--
```


                                                  
                      
