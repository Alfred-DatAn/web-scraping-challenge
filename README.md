# web-scraping-challenge

The present project consists on two main parts:

### 1.Web scraping
__mission_to_mars.ipynb__ which contains the code used to scrape from different web sites to get today's info about Mars. Then that code was converted into a function in __scrape_mars.py__.

### 2.App with Flask and PyMongo
__app.py__ renders the __index.html__ file, where you can request the Mars report. The button triggers the web scrapping function, push the resulting data to Mongo and finally the html file pull the results from the database.

Thanks!
