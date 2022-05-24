import json


f = open('updated-file_real.json', 'r')
write = open('../processed/test.json', 'w', encoding='utf-8')
data = json.load(f)

for i in data['data']:
    if ("Variety" and "Process" and "Altitude" and "Flavors" and 'Region') in i.keys():
        str = "Region: " + i['Region'] + ', ' "Variety: " + i['Variety'] + ', ' + "Altitude: " + i['Altitude']\
            + ', ' + "Process: " + i['Process']
        
        flavor = "Flavors: " + i['Flavors'] + '\n'

        entry = {"prompt": str, "completion": flavor}
        json.dump(entry, write, ensure_ascii=False)
        write.write('\n')

    else:
        continue

f.close()