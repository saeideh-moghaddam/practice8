def show_menu():
    print("1. Addition of complex numbers")
    print("2. Subtraction of complex numbers")
    print("3. Multiply complex numbers")
    print("4. exit")



def sum_complex(first_number,second_number):
    res={}
    res["r"]=first_number["r"] + second_number["r"],
    res["m"]=first_number["m"] + second_number["m"]
    return res

def sub_complex(first_number,second_number):
    res={}
    res["r"]=first_number["r"] - second_number["r"],
    res["m"]=first_number["m"] - second_number["m"]
    return res

def mult_complex(first_number,second_number):
    res={}
    res["r"]=first_number["r"] * second_number["r"],
    res["m"]=first_number["m"] * second_number["m"]
    return res

    #real_part =int(input(" please type real_part:"))
    #imaginary_part = int(input(" please type imaginary_part:"))
    #first_number = {"real_part": real_part,
    #                "imaginary_part": imaginary_part}

    # real_part2=int(input(" please type real_part:"))                                                
    # imaginary_part2 = int(input("please type imaginary_part:"))
    # second_number= {"real_part": real_part2,
    #                "imaginary_part": imaginary_part2}
    # result = mult(first_number,second_number)      
    # print((result ) , "i")       

real={"r":real_part , "m":imaginary_part}
imaginary={"r":real_part2 , "m":imaginary_part2}

show_menu()


select=int(input("please select a number :" ))
    
if select==1:
    sum=sum_complex(real,imaginary)
    print(sum)
elif select==2:
    sub=sub_complex(real,imaginary)
    print(sub)
elif select==3:
    mul=mult_complex(real,imaginary)
    print(mul)
elif select==4:
    exit()

real_part =int(input(" please type real_part:"))
imaginary_part = int(input(" please type imaginary_part:"))
real_part2=int(input(" please type real_part:"))                                                
imaginary_part2 = int(input("please type imaginary_part:"))  