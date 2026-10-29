mebleg = float(input("sifarisin meblegini daxil edin: "))
if mebleg < 0:
   print("Xeta : mebleg menfi ola bilmez.")
elif mebleg >= 200:
    endirim = mebleg * 0.20
    yekun = mebleg * endirim
    print("20% endirim qazandiniz.")
    print("yekun mebleb:", yekun ,"AZN")
elif mebleg > 100 and mebleg < 199.99:
    endirim = mebleg *0.10
    yekun = mebleg * endirim
    print("yekun mebleg: ", yekun,"AZN")
else:
    print ("endirim yoxdur.")
    print ("yekun mebleg:", mebleg , "AZN")

status = ("endirm qazandiniz") if mebleg >= 100 else ("endirim yoxdur")
print ("status: ", status)

