import random

judge = random.randint(1,2);

user = input("请输入0:剪刀，1:石头，2:布\n")

if user != "1" and user != "0" and user!= "2":
    print("您输入的不为目标数字")
else:
    user = int(user)
    if user == judge:
        print("平局")
    else:
        if (user == 0 and judge == 1) or (user == 1 and judge == 2) or (user == 2 and judge == 0):
            print("输了")
        else:
            print("赢了")