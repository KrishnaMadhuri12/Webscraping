#UseCase:
# Get data from fandango website through rest call
# Filter the data.


#IMPORTS : DEPENDENCIES
import requests
import bs4
from bs4 import BeautifulSoup
import json


#TASK1: Make Rest Api Call
#https://www.imdb.com/search/title?user_rating=8.6,10.0&genres=adventure,comedy,drama,family,romance

categories =[]
categories.append("adventure,comedy,drama,family,romance")
categories.append("adventure")
categories.append("comedy")
categories.append("drama")
categories.append("family")
categories.append("romance")


#Krishna Testing Collections
#categories ={"A":"adventure,,drama,family,romance","C":"comedy","D":""}

def get_URL(rating,category):
    URL="https://www.imdb.com/search/title?user_rating="+rating+"&genres"+category
    page= requests.get(URL)
    return BeautifulSoup(page.text,'html.parser')

#TASK2: Generate JSON object storing info movie title, year, rating,  intro
def get_movie_info(soup):
    total_items= soup.find_all(name="div",attrs={"class":"desc"})
    #print(total_items)
    array_data=[]
    for list in soup.find_all(name="div", attrs={"class":"lister-item-content"}):
        h3=list.find(name="h3",attrs={"class":"lister-item-header"})
        name=h3.find('a').text
        year=h3.find("span",attrs={"class":"lister-item-year text-muted unbold"})
        ratings=list.find(name="div",attrs={"class":"inline-block ratings-imdb-rating"})
        rating=ratings["data-value"]
        intro=list.find_all(name="p",attrs={"class":"text-muted"})
        movie_intro=intro[1].text.strip()
        #create the json dump
        data_obj={"name":name,"year":year.text,"ratings":rating,"intro":movie_intro}
        array_data.append(data_obj)
    return json.dumps(array_data)

#TASK3: Input Methods
#1. Method which lets user select the category number
def get_input_from_user():
    inc=0
    print('Available categories')
    for category in categories:
        print("{} {}".format(inc,category))
        inc=inc+1
    return int(input("Please provide selection"))


selected = get_input_from_user()
print(selected)
#2. get_URL

page_text=get_URL('8.6,10.0',categories[selected])
#3. get_movie_info
json_obj=get_movie_info(page_text)
print(json_obj)



