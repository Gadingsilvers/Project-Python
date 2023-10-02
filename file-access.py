devices=[]
file = open("coding-1.py" ,"r")
for item in file:
    item=item.strip()
    devices.append(item)
file.close()
print (devices)
