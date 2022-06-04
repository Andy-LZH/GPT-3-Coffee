import glob
import json

allData = []
for f in glob.glob("./processed_dumps/*.json"):
    with open(f, "r") as infile:
        data = json.load(infile)
        allData.extend(data["data"])


output = {}
output["data"] = allData
#with open("merged_file.json", "w", encoding="utf-8") as outfile:
#    json.dump(output, outfile, ensure_ascii=False)
with open("merged_file.json", "w") as outfile:
    json.dump(output, outfile, ensure_ascii=False)
