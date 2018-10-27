#UseCase: Fetch the current movies in amc theatres and store that to csv
#TASK1: Get data from url
#TASK2: Fetch the movie names
#TASK3: Store them in csv
import requests
import bs4
import csv
from bs4 import BeautifulSoup

#TASK1: Get data from url
URL ="https://www.amctheatres.com/"
page = requests.get(URL)
#print(page)
soup=BeautifulSoup(page.text,'html.parser')
#Below Prints the page html code
#print(soup.prettify())

#Below method fetches the page title
def extract_page_title_from_result(soup):
    return soup.title.string
#print('page tile is {}'.format(extract_page_title_from_result(soup)))

#TASK2: Fetch the movie names
def extract_page_movie_list_from_result(soup):
    movies=[]
    for element in  soup.find_all(name="li", attrs={"class":"Slide is-inactive hack-disableTransitions"}):
        for div in element.find_all(name="div", attrs={"class":"PosterSlide"}):
            for a in div.find_all(name="a",attrs={"class":"Link"}):
                movies.append(a["aria-label"])
    return(movies)

movies_from_url = extract_page_movie_list_from_result(soup)

def print_the_movies(movies):
    for movie in movies:
        print(movie)

print_the_movies(movies_from_url)

#TASK3: Store them in csv
def write_to_csv(movies):
    with open('movies.csv','w', newline='') as csvfile:
        #filewriter = csv.writer(csvfile, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
        filewriter = csv.writer(csvfile, dialect='excel')
        filewriter.writerow(["AMC Movie List"])
        for movie in movies:
            filewriter.writerow([movie])

write_to_csv(movies_from_url)
#A Star Is Born