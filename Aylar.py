def switch(ay):
    if ay == "Yanvar":
        return "Yanvar --- 31--gun"
    elif ay == "Fevral":
        return "Fevral --- 28--gun"
    elif ay == "Mart":
        return "Mart --- 31--gun"
    elif ay == "Aprel":
        return "Aprel --- 30--gun"
    elif ay == "May":
        return "May --- 31--gun"
    elif ay == "Iyun" :
        return "Iyun --- 30--gun"
    elif ay == "Iyul":
        return "Iyul --- 30--gun"
    elif ay == "Avqust":
        return "Avqust --- 31--gun"
    elif ay == "Sentyabr":
        return "Sentyabr --- 30--gun"
    elif ay == "Oktyabr":
        return "Oktyabr --- 31--gun"
    elif ay == "Noyabr":
        return "Noyabr --- 30--gun"
    elif ay == "Dekabr":
        return "Dekabr --- 31--gun"

print("Ay Nomresi Daxil Edin: ")
proses=int(input())
if proses == 1:
    print(switch("Yanvar"))
elif proses == 2:
    print(switch("Fevral"))
elif proses == 3:
    print(switch("Mart"))
elif proses == 4:
    print(switch("Aprel"))
elif proses == 5:
    print(switch("May"))
elif proses == 6:
    print(switch("Iyun"))
elif proses == 7:
    print(switch("Iyul"))
elif proses == 8:
    print(switch("Avqust"))
elif proses == 9:
    print(switch("Sentyabr"))
elif proses == 10:
    print(switch("Oktyabr"))
elif proses == 11:
    print(switch("Noyabr"))
elif proses == 12:
    print(switch("Dekabr"))
else:
    print("Ay Duzgun Daxil Edilmeyib")
