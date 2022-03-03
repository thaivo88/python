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
<b>headers = {'Accept': 'application/vnd.github.v3+json'}</b>
GitHub is currently on the third version of its API, so we define headers for the API call w that ask explicitly to use this version of the API.
Then we use <i>requests</i> to make the call to the API
We call <i>get()</i> and pass it the URL and the header that we defined, and we assign the response object to the variable <i>r</i>.
The response object has an attribute called <i>status_code/i>, which tells us whether the request was successful. (A status code of 200 indicates a successful response.)
The API returns the information in JSON format, so we use the <i>json()</i> method to convert the information to a Python dictionary. We store the resulting dictionary in <i>response_dict</i>.

  
  
