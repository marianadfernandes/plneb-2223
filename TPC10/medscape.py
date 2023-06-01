import requests
import json
import re
from bs4 import BeautifulSoup

def BSParser(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html,"html.parser")
    return soup, url

def getAncorsInLists(division):
    ancors = []
    titles = []
    lists = division.find_all("li")
    for list in lists:
        text = list.text
        ancor = list.a["href"] 
        ancors.append(ancor) 
        titles.append(text)
    return titles, ancors

soup, url = BSParser("https://reference.medscape.com/")

divs = soup.find_all("div", id="dd-explore")

# get the urls to another page
doc = []
urls = []
for div in divs:
    second_div = div.find("div", class_="section-content")
    text, ancors = getAncorsInLists(second_div)
    for ancor in ancors:
        if re.search("//", ancor) :
            second_url = url[:-1] + ancor[1:]
        else:
            second_url = url[:-1] + ancor
        #doc.append({text : second_url})
        urls.append(second_url)

  
soup_, second_url = BSParser(urls[0])
third_div = soup_.find("div", id="drugdbmain2")
title, new_ancors = getAncorsInLists(third_div)

#third page
soup_3, third_url = BSParser(new_ancors[0])
fourth_div = soup_3.find("div", class_="topic-list sections active")
title2, new_new_ancors = getAncorsInLists(fourth_div.div.div)

for t in text:
    doc.append({t: 0}) 

aux_list = []
for key, value in doc[0].items():
    for t1 in title:
        aux_list.append({t1:0})
    doc[0][key] = aux_list

aux_list2 = []
for t in doc[0].values():
    for key, value in t[0].items():
        for t2, a in zip(title2, new_new_ancors):
            aux_list2.append({t2:a})
    t[0][key] = aux_list2
           

file = open("medscape.json","w", encoding="utf8")
json.dump(doc,file, ensure_ascii=False, indent = 4)
file.close()
