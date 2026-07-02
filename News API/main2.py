import requests # pip install request 
#> https://pypi.org/project/requests/

query = input('What type of News are you interested in today:')
api = "99b2644492854492bc7a05ce944078e7"


url = f'https://newsapi.org/v2/everything?q={query}&from=2026-06-02&sortBy=publishedAt&apiKey={api}'

print(url)

r = requests.get(url)

data = r.json()

articles = data['articles']

for index, article in enumerate(articles):
    print(index+1,article['title'] , article['url'])

    print('\n********************************************\n')


    # Requests
''' GET — you're asking the server to give you something. Think of it like asking a hotel front desk: "What rooms are available?" You're not handing over any data to be stored — you're just requesting information. That's why your NewsAPI call is a GET: you're asking for articles, not sending any.
POST — you're asking the server to accept and do something with data you're sending. Think of it like filling out a guest registration form at check-in — you're submitting information (name, ID, payment details) for the hotel to store and act on.'''

'''# GET - retrieving data, parameters usually go in the URL
r = requests.get(url)

# POST - sending data, parameters go in the request body
r = requests.post(url, json={"name": "Abhishek", "email": "abc@example.com"})'''

# %% [markdown]
"""
KEY PRACTICAL DIFFERENCES: GET vs POST
======================================
| Feature            | GET                          | POST                          |
|--------------------|------------------------------|-------------------------------|
| Purpose            | Retrieve data                | Submit/create data            |
| Data location      | URL (?q=news&from=2026-06-02)| Request body (hidden)         |
| Visible in history?| Yes                          | No                            |
| Bookmarkable?      | Yes                          | No                            |
| Cacheable?         | Yes                          | No                            |
| Typical use cases  | Search, fetch articles,      | Login, form submit,           |
|                    | view profile                 | create record, upload file    |
======================================
"""