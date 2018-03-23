#download
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url ='http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn'
cafef_content = urlopen(url).read().decode('utf8')

#ROI
soup = BeautifulSoup(cafef_content, 'html.parser') #xml,xhtml,

tr = soup.find('tr', 'r_item ')

# Extract Info
tr_list = tr.find_all('td')
for td in tr_list:
    print(td.prettify())
    print('* ' * 30)


datas=[]
column = ['Trước   Sau','Quý 4-2016','Quý 1 -2017','Quý 2 -2017','Quý 3 -2017']
for tr in tr_list:
    data={}
    for i in range(len(column)):
        data[column[i]] = tr_list[i].string
    datas.append(data)

pyexcel.save_as(records= datas, dest_file_name="cafef.xlsx")
