#Q5- Dictionary 

#Python Code-
dt = {
    "Name": "Alok",
    "Age": 21,
    "Place": "BBSR"
}
print(dt["Name"])
print(dt["Age"])

dt["Email"] = "jitenalok03@gmail.com"

dt["Age"] = 24

del dt["Place"]

for key, value in dt.items():
    print(key, value)


# Output
# Alok
# 21
# Name Alok
# Age 24
# Email jitenalok03@gmail.com
