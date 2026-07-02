query = 'Artificial Intelligence'
api = "99b2644492854492bc7a05ce944078e7"


url = f'https://newsapi.org/v2/everything?q={query}&from=2026-06-02&sortBy=publishedAt&apiKey={api}'

print(url)

# if copy paste the link from terminal after runing the code on crome it will be in single line messy format.
#To make it readable we will install json pretty formatter from google as an extension
# then it will show json format (dictionary)
***************************************************************
# crlt + , = setting 
# all text on one page with vertical slider = wrod wrap(setting) - on

# not all the url seems similar to this where some will represent lat long ex weather forcasting. and etc.

'''1. By city name (what I showed earlier):
https://api.openweathermap.org/data/2.5/weather?q=Jaipur&appid=YOUR_KEY'''

'''2.By coordinates (what you're seeing now):
https://api.openweathermap.org/data/2.5/weather?lat=26.9124&lon=75.7873&appid=YOUR_KEY'''

'''3.By city ID (another option in their docs):
https://api.openweathermap.org/data/2.5/weather?id=1269515&appid=YOUR_KEY'''

'''4.By zip code:
https://api.openweathermap.org/data/2.5/weather?zip=302001,in&appid=YOUR_KEY'''

