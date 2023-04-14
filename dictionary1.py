#  Dictionary ->{},order collection of datatypes ,doesnt contain duplicate values,key and values,mutable
mydic={
    "Username":"Admin",
    "Password":1234,
    "Batch":2023
}
# update
mydic["Password"]=890
print("The values are ",mydic)
mydic["Username"]="abc@gmail.com"
print("The values are",mydic)
print(type(mydic))
print(len(mydic))
