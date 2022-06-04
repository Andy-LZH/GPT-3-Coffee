#Species ?? , Country, Altitude, Region, Variety, Processing Method, flavor

from concurrent.futures.process import _ResultItem
import requests
import re
from bs4 import BeautifulSoup
import csv
import json

output_file_name = 'royalcoffee_dataset.json'
URL = "https://royalcoffee.com/offerings/page/"

#url = "https://royalcoffee.com/product/3427097000009452990/" 

#San Marcos de Tarrazú, San José, Costa Rica
# Function which returns last word
#Returns Costa Rica
"""
def lastword(string):
    lis = string.rsplit(',', 1)[1]
    return lis

 
#Returns Rica
    # split by space and converting
    # string to list and
    lis = list(string.split(" "))
     
    # length of list
    length = len(lis)
     
    # returning last element in list
    return lis[length-1]
"""

def extractInfo(url):
    result = {}
    #result["url"] = url
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        #print(soup) 
        job_elements = soup.find_all("div", class_="royal-coffee origin")
        tableDiv = job_elements[0].findChildren('div', recursive=False)[0].findChildren('div', recursive=False)

        for tableData in tableDiv:
            try:
                label = tableData.contents[0].text
                desc = tableData.contents[1].text
                #preprocess
                if((label == "Grower") or (label == "Harvest") or (label == "Soil") or (label == "Certifications")):
                    continue
                """
                if label == 'Region' :
                    #print("before" + " " + desc)
                    country = lastword(desc)
                    
                    #print(country)
                    result['Country'] = country
                    desc = desc.replace(', '+country,'')  
                    #print("after" + " " + desc)
                """                      
                result[label] = desc
            except:
                print("Error for Url" + url)
        #read flavors
        job_flavors = soup.find_all("p", class_="characteristics")
        for jobflavor in job_flavors:
            try:
                #print(jobflavor.text)
                #jobflavor = jobflavor.text.strip('\n')
                #jobflavor = jobflavor.text.strip('\t')
                #string = jobflavor.text
                #string = string.lstrip()
                #string = string.replace('\n',"")
                #string = string.replace('\t',"")
                #string = string.trim()
                #string = string.lstrip()
                #result['Flavors'] = string
                #result['Flavors'] = jobflavor.text
                result['Flavors'] = jobflavor.text.strip('\n')
                #print(result['Flavors'])

            except:
                print("Error for Url" + url)
                    
    except:
        print("Error for Url" + url)
    
    return result

def getlinks(URL):
    #print("URLs on Page: :", URL)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    result = []
    index = 1
    for a in soup.find_all('a', href=True):
        #print ("Found the URL:", a['href'])
        # Filter
        if(a and a['href'] and a['href'].startswith("https://royalcoffee.com/product/")):
            #print ("Found the URL " + str(index) + ":" , a['href'])
            index += 1
            
            result.append(extractInfo(a['href']))
    return result

#pages 1 - 26 range(1,27)
for p in range(1, 27):
    output = {}
    output["data"]  = getlinks(URL+ str(p))
    print("Processing " + URL + str(p))
    
    with open(str(p) + output_file_name, 'w', encoding='utf8') as outfile:
        json.dump(output, outfile, ensure_ascii=False)

        #with open(str(p) + output_file_name, 'w', encoding='utf8') as outfile:
    #    json.dump(output, outfile, ensure_ascii=False)
    



#print(json.dumps(output))

#extractInfo(url)

#print(soup) 

#document.querySelector("#left-area > ul")

#job_elements = results.find_all("div", class_="a")
#for elem in soup.find_all('a', href=re.compile('http://www\.iwashere\.com/')):
#<a href="http://www.iwashere.com/washere.html">next</a>
#https://royalcoffee.com/product/3427097000009457211/

#soup.find('a', {'href': "http://www.iwashere.com/"}, partial=True)


