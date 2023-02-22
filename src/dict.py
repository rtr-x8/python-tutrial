a = {
    "name": "name",
  "val": "vvv"
}

print(a.get("name"))
print(a["name"])
#print(a.get("aaa")) # return None
#print(a["aa"]) # thorow error


a.update({'name': 'Makemake'})
print(a)

a["name"] = "abcs"
a["aaa"] = "abcs"
print(a)

a.pop('name')
print(a)

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

print(rainfall.keys())
print("aaa" in rainfall.keys())

print(rainfall.values())