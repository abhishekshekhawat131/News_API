News API Fetcher

A simple Python script that fetches live news articles from NewsAPI.org based on a topic entered by the user, and prints the article titles and links.

What it does


Asks the user what kind of news they're interested in
Builds a NewsAPI query URL with that topic
Sends a GET request to NewsAPI and parses the JSON response
Prints the title and URL of each returned article


Tech Stack


Python 3
requests library for the HTTP call


How to run

bashpip install requests
python main2.py

You'll be prompted to enter a news topic, and it will print the latest matching articles.

What I learned: GET vs POST

FeatureGETPOSTPurposeRetrieve dataSubmit / create dataData locationURLRequest body (hidden)Visible in history?YesNoBookmarkable?YesNoCacheable?YesNoTypical use casesSearch, fetch articles, view profileLogin, form submit, create record, upload file

Hotel front-desk analogy: GET is like asking the front desk "what rooms are available?" — you're only asking for information. POST is like filling out a guest registration form at check-in — you're submitting data for the hotel to store and act on.

This NewsAPI call is a GET, since we're only retrieving articles.

Author

Abhishek Singh Shekhawat
GitHub
