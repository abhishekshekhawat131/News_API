# News API Fetcher

A simple Python script that fetches live news articles from [NewsAPI.org](https://newsapi.org) based on a topic entered by the user, and prints the article titles and links.

## What it does

- Asks the user what kind of news they're interested in
- Builds a NewsAPI query URL with that topic
- Sends a `GET` request to NewsAPI and parses the JSON response
- Prints the title and URL of each returned article

## Tech Stack

- Python 3
- [`requests`](https://pypi.org/project/requests/) library for the HTTP call

## How to run

```bash
pip install requests
python main2.py
```

You'll be prompted to enter a news topic, and it will print the latest matching articles.

## What I learned: GET vs POST

| Feature              | GET                                   | POST                                     |
|-----------------------|----------------------------------------|--------------------------------------------|
| Purpose               | Retrieve data                          | Submit / create data                       |
| Data location         | URL                                     | Request body (hidden)                       |
| Visible in history?   | Yes                                    | No                                          |
| Bookmarkable?         | Yes                                    | No                                          |
| Cacheable?            | Yes                                    | No                                          |
| Typical use cases     | Search, fetch articles, view profile   | Login, form submit, create record, upload file |

**Hotel front-desk analogy:** GET is like asking the front desk "what rooms are available?" — you're only asking for information. POST is like filling out a guest registration form at check-in — you're submitting data for the hotel to store and act on.

This NewsAPI call is a GET, since we're only retrieving articles.

## Author

**Abhishek Singh Shekhawat**
[GitHub](https://github.com/abhishekshekhawat131)
