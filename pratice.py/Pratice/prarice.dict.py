dict = {"kunal": 99,
        "gannu": 100,
        "tanu":78}

print(dict.items())
print(dict.keys())
print(dict.values())
print("you got ", + dict.get("kunal"))


# for Sets 

sets = {1,2,3}
sets.add(3)
print(3 in sets)
print(sets)

print("yes") if 3 in sets else print("No")

for i in dict:
    print(i)