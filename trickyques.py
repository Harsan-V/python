students = [
    {"name ":"raju","dept":"csc","marks":[20,30,40]},
    {"name ":"vijay","dept":"csc","marks":[10,70,43]},
    {"name ":"pavi","dept":"ece","marks":[22,38,56]},
    {"name ":"rose","dept":"ece","marks":[26,36,89]},
    {"name ":"rvirat","dept":"ece","marks":[16,90,43]},
]
for i in students:
    tot = sum(i["marks"])
    avg = tot//3
    i["percentage"] = avg

students.sort(key = lambda x:x["percentage"], reverse=True)

pos = ["first","second","third","fourth","fifth"]
j = 0
for i in students:
    print("{} scored {} % --> stands {}".format(i["name"],i["percentage"],pos[j]))
    j = j+1
print(students)

