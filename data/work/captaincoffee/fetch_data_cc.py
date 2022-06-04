#Species ?? , Country, Altitude, Region, Variety, Processing Method, flavor

from concurrent.futures.process import _ResultItem
import requests
import re
from bs4 import BeautifulSoup
import csv
import json

output_file_name = 'coffeecaptain_dataset.json'
URL = "https://thecaptainscoffee.com/collections/green-coffee"

#url = "https://royalcoffee.com/product/3427097000009457220/" 

"""
# Function which returns last word
def lastword(string):
   
    # split by space and converting
    # string to list and
    lis = list(string.split(" "))
     
    # length of list
    length = len(lis)
     
    # returning last element in list
    return lis[length-1]
"""
#div.contents[1].find_all('p')[4].text.replace(u'\xa0', u' ').replace(u'\ufeff', u' ').split(':')[0]

def extractInfo(url):
    print(url)
    result = {}
    #result["url"] = url
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        div = soup.find("div", {"id": "collapse-tab1"})

        tableDiv = div.contents[1].find_all('p')
        for p in range(1,len(tableDiv)):  
            try:
                text = tableDiv[p].text

                #preprocess
                text = tableDiv[p].text.replace(u'\xa0', u'').replace(u'\ufeff', u'')
                
                if(not text):
                    continue
                split = text.split(':')

                if(len(split) < 2):
                    continue
                
                label = split[0]
                desc = split[1]

                if(label == "Our Review"):
                    continue

                if(label == "Our Review"):
                    continue
                #preprocess 
                if(label == "Flavor Traits"):
                    label = "Flavors"
                if(label == "Grade"):
                    label = "Altitude"
                if(label == "Processing"):
                    label = "Process"    
                if(label == "Varietals"):
                    label = "Variety"    
                if(label == "Varieties"):
                    label = "Variety"     

                if((label == "Flavors") or (label == "Altitude") or (label == "Process") or (label == "Variety") or (label == "Region")):
                    result[label] = desc
                else:
                    continue

            except :
                print("Error for Div:" + p)     
    except:
        print("Error for Url:" + url)

    return result
    

def getlinks(URL):
    #print("URLs on Page: :", URL)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    #print(soup)
    
    result = []
    index = 1
    
    processedSet = {''}
    for a in soup.find_all('a', href=True):
        if(a and a['href'] and a['href'].startswith("/collections/green-coffee/products")):
            
            index += 1
            producturl = 'https://thecaptainscoffee.com/' + a['href']
            
            if(a['href'] in processedSet):
                continue
            processedSet.add(a['href'])
            result.append(extractInfo(producturl))
    return result


def process(URL):
    output = {}
    output["data"]  = getlinks(URL)
    #print(output)

    with open(output_file_name, 'w', encoding='utf8') as outfile:
            json.dump(output, outfile, ensure_ascii=False)

process(URL)
# test
#print(json.dumps(extractInfo("https://thecaptainscoffee.com//collections/green-coffee/products/colombia-tolima-gaitania-organic")))



#getlinks(URL)

#print(json.dumps(output))

#extractInfo(url)

#print(soup) 

#document.querySelector("#left-area > ul")

#job_elements = results.find_all("div", class_="a")
#for elem in soup.find_all('a', href=re.compile('http://www\.iwashere\.com/')):
#<a href="http://www.iwashere.com/washere.html">next</a>
#https://royalcoffee.com/product/3427097000009457211/

#soup.find('a', {'href': "http://www.iwashere.com/"}, partial=True)