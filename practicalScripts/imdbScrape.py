from requests import get
from bs4 import BeautifulSoup
import csv

url = 'http://www.imdb.com/chart/top?ref_=nv_mv_250_6'

response = get(url)

#print(response.text[:200])

html_soup=BeautifulSoup(response.text,'html.parser')


#movie_containers = html_soup.find_all('tbody',class_='lister-list')
movie_containers = html_soup.find_all('td',class_='titleColumn')
movie_ratings = html_soup.find_all('td',class_='ratingColumn imdbRating')
movieDict = {}
average_rating = 0
movies = []
ratings =[]
with open('movies.txt','w') as f,open('ratings.txt','w') as f_out:
    for i in range(250):
        movies.append(movie_containers[i].a.text)
        ratings.append(movie_ratings[i].strong.text)
        f.write(movies[i]+"\n")
        f_out.write(ratings[i]+"\n")
        movieDict[movies[i]]=float(ratings[i])
        average_rating+=float(ratings[i])

#print(average_rating/250)
#print(movieDict)
print(movieDict)
above=[]
#with open('movies.txt','r') as f,open('ratings.txt','r') as f_in:
   # print(f.read())
with open('top250.csv', 'w') as f:
    [f.write('{0},{1}\n'.format(key, value)) for key, value in movieDict.items()]



#print(len(movie_containers))
#print(len(movie_ratings))
#first_movie = movie_containers[0].tr.find('td',class_='titleColumn').a.text

#print(first_movie)
