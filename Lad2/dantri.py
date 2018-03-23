#download
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url ='http://dantri.com.vn/'
html_content = urlopen("http://dantri.com.vn").read().decode('utf8')

#saving html_content to file
# html_file = open('dantri.html', 'w')
# html_file.write(html_content)
# html_file.close()


#ROI lay vung chon
soup = BeautifulSoup(html_content, 'html.parser') #xml,xhtml,
# print(soup.prettify()) #prettify lam dep Code

ul = soup.find('ul', 'ul1 ulnew') #(the, gia tri cua the) cho class
# print(ul.prettify())

#Extract Info
li_list = ul.find_all('li')
# for li in li_list:
#     print(li.prettify())
#     print('* ' * 30)


datas = []

for li in li_list:
    data = {}
    a = li.h4.a
    data['title'] = a.string
    data['link'] = url + a['href']
    datas.append(data)

pyexcel.save_as(records= datas, dest_file_name="dantri.xlsx")
