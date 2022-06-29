def sum(number1,number2):
   dictionary={} 
   dictionary["numerator"] = number1["numerator"] * number2["Denominator"] + number1["Denominator"] * number2["numerator"]
   dictionary["Denominator"] = number1["Denominator"] * number2["Denominator"]
   return dictionary

def mult(number1,number2):
   dictionary={} 
   dictionary["numerator"] = number1["numerator"] * number2["numerator"]
   dictionary["Denominator"] = number1["Denominator"] * number2["Denominator"]
   return dictionary

def div(number1,number2):
    dictionary={}
    dictionary["numerator"]= number1["numerator"] * number2["Denominator"]
    dictionary["Denominator"]= number1["Denominator"] * number2["numerator"]
    return dictionary

def sub(number1,number2):
    dictionary={}
    dictionary["numerator"]= number1 ["numerator"] * number2 ["Denominator"] - number1["Denominator"] * number2["numerator"]
    dictionary["Denominator"]= number1["Denominator"] * number2["Denominator"]
    return dictionary

First_fraction  = {"numerator" : 5 , "Denominator" : 7} 
Second_fraction  = {"numerator" : 8 , "Denominator" : 9} 

result =("Answer the sum of fractions :" , sum(First_fraction,Second_fraction),
"Answer Multiply fractions :" , mult(First_fraction,Second_fraction),
"Answer division fractions :" , div(First_fraction,Second_fraction),
"Answer submission fractions :" , sub(First_fraction,Second_fraction)) 
print(result)