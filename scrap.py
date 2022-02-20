#This program is for scrapping from web
#We are going to use Beautiful Soup to scrap the web data
#Also we are going to use requests module
from bs4 import BeautifulSoup
import requests,openpyxl
#Excelfile module
excel=openpyxl.Workbook()
sheet =excel.active
sheet.title='Top Rated Movies'
sheet.append(['Movie Rank',"Movie Name","Year of Release","IMDB rating"])

try:
    source=requests.get('https://www.imdb.com/chart/top/')
    source.raise_for_status() #send an Error Massaage if website is not found
    soup=BeautifulSoup(source.text,'html.parser')
    movies=soup.find('tbody',class_="lister-list").find_all('tr')
    for movie in movies:
        name=movie.find('td',class_="titleColumn").a.text #tag.text used to access only text of the tag
        rank=movie.find('td',class_="titleColumn").get_text(strip=True).split(".")[0]
        year=movie.find('td',class_="titleColumn").span.text.strip('()')
        rating=movie.find('td', class_='ratingColumn imdbRating').strong.text
        print(rank,name,year,rating)
        sheet.append([rank,name,year,rating])
except Exception as e:
    print(e)
excel.save('IMDB rating.xlsx')
