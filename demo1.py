db = [{"username":"hello kutty", "password":"123456"}, {"username":"大熊", "password":"654321"}]
mz = input("please input your name: ")
mm = input("please inoput your password: ")
count = 1
for i in db:
    if mz == i.get("username"):
        i["password"]=mm
        break
    else:
        if len(db) == count:
            db.append({"username":mz,"password":mm})
    count = count + 1
print(db)
        