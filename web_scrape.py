from bs4 import BeautifulSoup
import requests
import csv 


source = requests.get('https://kun.uz/uz/news/2023/08/04/cobalt-lacetti-va-damas-sotuvi-8-oy-deganda-tiklandi').text

csv_file = open('mashina_sotuv.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headers', 'text', 'image_link','date'])




soup = BeautifulSoup(source, 'lxml')

header_1 = soup.find(class_ = 'single-header__title').text

header_4 = soup.find('div', class_ = 'single-content').h4.text

main_img_url = soup.find('div', class_ = 'main-img').img['src']

content_div = soup.find('div', class_ = 'single-content')

p_txt = ' '.join([p.text for p in content_div.find_all('p')])

li_txt = ' '.join([li.text for li in content_div.find_all('li')])

date = soup.find('div', class_ = 'date').text

csv_writer.writerow([[header_1,header_4],[p_txt,li_txt],main_img_url,date])

csv_file.close()

