__author__ = 'Dell'
import requests,os
from bs4 import BeautifulSoup




url = 'https://github.com/trending?l=python'
r = requests.get(url)

soup = BeautifulSoup(r.content)

get_data = soup.find_all('h3',{'class':'repo-list-name'})

os.chdir('/home/ubuntu/pcr/get_git')
for link in get_data:
    a_link = link.find_all('a')
    comad = 'git clone'
    for href_link in a_link:
        git_repo_name = href_link.get('href')
        git_repo_url = 'https://github.com' + git_repo_name
        comad = comad + '\t' + git_repo_url
        os.system(comad)



