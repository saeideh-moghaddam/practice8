import math
import time
def sum(a,b):
     time={}   
     time["S"] = a["S"] + b["S"]
     time["M"] = a["M"] + b["M"]
     time["H"] = a["H"] + b["H"]    
     if time ["S"]>= 60:
         time["S"] -= 60
         time["M"] += 1

     if time ["M"]>= 60:
        time["M"] -= 60
        time["H"] += 1
     return time

def Show(show):
    print(show["H"], ":", show["M"], ":", show["S"])
    
num1 = {"H":10, "M":20, "S":40}    
num2 = {"H":8, "M":30, "S":30}
num3 = sum(num1, num2)
Show(num3)
 

def sub(a,b):
    time={}   
    time["S"] = a["S"] - b["S"]
    time["M"] = a["M"] - b["M"]
    time["H"] = a["H"] - b["H"]    

    if time ["S"] <0:
        time["M"] -= 1
        time["S"] += 60

    if time ["M"] <0:
        time["H"] -= 1
        time["M"] += 60
        return time

def Show(show):
    print(show["H"], ":", show["M"], ":", show["S"])
    
num1 = {"H":10, "M":20, "S":40}    
num2 = {"H":8, "M":30, "S":30}
num3 = sub(num1, num2)
Show(num3)




def the_time():
    S = int(input("please type the second : "))
    H = (S // 3600)
    M = (S % 3600) //60
    S = (S %3600)%60
    return H,M,S

def Show(show):
    print(show["H"],":",H , show["M"],":",M , show["S"],":",S)


H,M,S=the_time()  

print(H,M,S)

#Show()
# def second():
#     # H = int(input("please enter an hour = "))
#     # M = int(input("please enter a minute = "))
#     # S = int(input("please enter a second = "))
#     return H,M,S 
# H = int(input("please enter an hour = "))
# M = int(input("please enter a minute = "))
# S = int(input("please enter a second = "))

# Hour = (H * 3600)
# Minute = (M * 60)
# watch= Hour + Minute + S 
# watch=second
# print(watch)


def second(x):
          
    second =(x['h']*3600 + x['m']*60 + x['s'])
    return second
def show(x):
    print(x["h"], ":", x["m"], ":", x["s"])
    num1 ={"h":3, "m":30, "s":45}
    num3={"h":13, "m":46, "s":30}
    num3= show(sum(num1, num2))
    print(num3)
    sub1=show(sub(num1,num2))
    print (sub1)
    s_to_h=show(the_time())
    print (s_to_h)
    h_to_s=second(num1)
    print(h_to_s)