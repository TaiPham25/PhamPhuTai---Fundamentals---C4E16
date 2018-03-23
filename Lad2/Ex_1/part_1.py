#download
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

url ='https://www.apple.com/itunes/charts/songs/'
itunes_content = urlopen(url).read().decode('utf8')

#ROI
soup = BeautifulSoup(itunes_content, 'html.parser') #xml,xhtml,

section = soup.find('section', 'section chart-grid')

# Extract Info
li_list = section.find_all('li')
for li in li_list:
    print(li.prettify())
    print('* ' * 30)


datas = []
for li in li_list:
    data = {}
    data['names'] = li.h3.a.string
    data['artists'] = li.h4.a.string
    datas.append(data)

pyexcel.save_as(records= datas, dest_file_name="itunes.xlsx")


options = {
    'default_search': 'ytsearch',
    'max_downloads': 1,
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
for li in li_list:
    song = li.h3.a.string
    artist = li.h4.a.string
    dl.download([song,artist])
