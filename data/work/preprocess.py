
# Load the JSON module and use it to load your JSON file.                       
# I'm assuming that the JSON file contains a list of objects.                   
import json
import numpy as np
import random


filename = 'merged_file.json' #real data - 1077
output_file_name = 'updated-file_real.json'


list1 = [] 
list2 = [] 
list3 = [] 
list4 = [] 
list5 = [] 


def addInfo():
     #print(list1)
     lists = {}
     sizeflavor = random.randint(1, 4)
     randfl = np.random.choice(list1, sizeflavor,replace=False)
     #print(randfl)
     randfl = ','.join(randfl.tolist())
     lists['Flavors'] = randfl
     #print(lists)
     randvariety = np.random.choice(list2)
     #randvariety = ','.join(randvariety.tolist())
     lists['Variety'] = randvariety
     #sizeregion = random.randint(1, 4)
     randregion = np.random.choice(list3)
     #randregion = ','.join(randregion.tolist()) 
     lists['Region'] = randregion
     #sizealt = random.randint(1, 4) 
     randalt = np.random.choice(list4)
     #randalt = ','.join(randalt.tolist()) 
     lists['Altitude'] = randalt
     #sizeproc = random.randint(1, 4) 
     randproc = np.random.choice(list5)
     #randproc = ','.join(randproc.tolist())        
     lists['Process'] = randproc
            

     return lists

#Remove empty List from List
def empty_list_remove(input_list):
    new_list = []
    for ele in input_list:
        if ele:
            new_list.append(ele)
    return new_list

def preprocess(filename):
    with open(filename, 'r+') as f:
        obj = json.load(f)

        list = obj["data"]
        list = empty_list_remove(list)

#get all the flavors from the dataset     
        for lists in list:
            value = lists.get('Flavors')    
            if(value):
                value = value.split(',')
                list1.extend(value)
        #print(list1)  



#fill in the empty data flavors from the obtained list1
                
        for lists in list:
            value = lists.get('Flavors')    
            if(value == ""):
                sizeflavor = random.randint(1, 4)
                randflavor = np.random.choice(list1, sizeflavor)
                randflavor = ','.join(randflavor.tolist())
                #print(randflavor)
                lists['Flavors'] = randflavor
                #lists.get('Flavors', var)
            #remove empty lists    
            #list = list(filter(None, lists))  

    #return list  
 
        ####  add 10,000 entries - toy dataset #### 
        
        #get all the Variety from the dataset    
        for lists in list:
            value = lists.get('Variety')    
            if(value):
                value = value.split(',')
                list2.extend(value)
        #print(list2)

        #get all the Region from the dataset   
        for lists in list:
            value = lists.get('Region')    
            if(value):
                value = value.split(',')
                list3.extend(value)
        #print(list3)

        #get all the Altitude from the dataset  
        for lists in list:
            value = lists.get('Altitude')    
            if(value):
                value = value.split(',')
                list4.extend(value)
        #print(list4)                

        #get all the Process from the dataset    
        for lists in list:
            value = lists.get('Process')    
            if(value):
                value = value.split(',')
                list5.extend(value)
        #print(list5)
        """
        for p in range(1, 10000):
            list.append(addInfo())
        """    


    return list

      


#print(obj["data"])

output = {}
output["data"]  = preprocess(filename)

with open(output_file_name, 'w', encoding='utf8') as outfile:
    json.dump(output, outfile, ensure_ascii=False)