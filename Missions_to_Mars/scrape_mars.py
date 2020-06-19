#Library
from splinter import Browser
from bs4 import BeautifulSoup as bs
import GetOldTweets3 as got
import pandas as pd

def scrape():

    #Route
    executable_path = {"executable_path": "chromedriver.exe"}
    #Browser assignation
    browser = Browser("chrome", **executable_path, headless=True)

    #NASA MARS NEWS---------------------------------
    browser.visit("https://mars.nasa.gov/news/")
    html = browser.html
    soup = bs(html, "html.parser")
    #look for the news elements
    news = soup.find_all("div", class_="slide slick-slide slick-active")
    #look for the the very fisrt linkable title
    title_link = news[0].find("div", class_="content_title").find("a").text[1:-1]
    #click the first news
    browser.links.find_by_text(title_link).click()

    #Retrieve the news html
    soup_news = bs(browser.html, "html.parser")
    news_title = soup_news.find("h1", class_="article_title").text[1:-1] #SSSSSSSS
    first_p = soup_news.find("div", class_= "wysiwyg_content").find_all("p")[1].text #SSSSSSSS


    #JPL MARS SPACE---------------------------------
    browser.visit("https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars")
    html_jpl = bs(browser.html, "html.parser")
    image_url = html_jpl.find("a", class_= "button fancybox")["data-fancybox-href"]
    featured_image_url = f"https://www.jpl.nasa.gov{image_url}" #SSSSSSSS


    #MARS HEMISPHERES---------------------------------
    browser.visit("https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars")
    html_hem = bs(browser.html, "html.parser")
    images = html_hem.find_all("div", class_="description")
    hem_list = [] #SSSSSSSS

    for image in images:
        url = image.find("a")["href"]
        title_img = image.find("h3").text
        browser.visit(f"https://astrogeology.usgs.gov{url}")
        hem_img = bs(browser.html, "html.parser")
        img_url = hem_img.find("div", class_="downloads").find("a")["href"]
        hem_list.append({"title": title_img, "img_url" : img_url})

    browser.quit()


    #MARS WEATHER TWITTER ACCOUNT---------------------------------
    #!pip install GetOldTweets3
    username = 'MarsWxReport'
    #Query object
    tweetCriteria = got.manager.TweetCriteria().setUsername(username).setMaxTweets(3)
    #Creation of list that contains all tweets
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    #Getting the last tweet
    last_tweet = tweets[0].text #SSSSSSSS


    #MARS FACTS---------------------------------
    tables = pd.read_html("https://space-facts.com/mars/")
    mars_table = tables[0].rename(columns={0: "Variable", 1: "Value"})

    html = mars_table.to_html(index = False, classes = "table_test")
    with open("templates/ttable.html", "w", encoding="latin-1") as file:
        #file.writelines('<meta charset="latin-1">\n')
        file.write(html)

    with open("templates/ttable.html", "r", encoding="latin-1") as f:
        ttext = f.read()


    #DASHBOARD---------------------------------
    dashboard = {}
    dashboard["news_title"] = news_title
    dashboard["news_text"] = first_p
    dashboard["image"] = featured_image_url
    dashboard["tweet"] = last_tweet
    dashboard["hemispheres"] = hem_list
    dashboard["table"] = ttext
 
    return dashboard

