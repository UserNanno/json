import json
# import requests
# from requests.structures import CaseInsensitiveDict

file = "dat.json"

# url = "https://api.geoapify.com/v1/geocode/autocomplete?text=Mall Sur&apiKey=3af67dc42b274747bde3dcf9528d79b8"
# headers = CaseInsensitiveDict()
# headers["Accept"] = "application/json"
 
# resp = requests.get(url, headers=headers)
 
with open(file, "r") as json_file:
    data = json.load(json_file)
    j = 0
    for i in data["features"]:
        formato = i["properties"]          
        print(f"Index number: {j}")
        print(formato)
        j = j + 1