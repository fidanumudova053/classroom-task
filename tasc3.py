gelir = float(input("ayliq gelirini daxil edin: "))
umumi_xerc = float(input("Umumi xercleri daxil edin: "))

if gelir<0 or umumi_xerc <0:
    print("Xeta: gelir ve xerc menfi ola bilmez.")

else:
    qalan = gelir - umumi_xerc
    faiz = (qalan/gelir)*100
    xerc_faizi = (umumi_xerc/gelir)*100
    if umumi_xerc> gelir:
        print("budce kesiri var")
    elif xerc_faizi >= 80:
        print("xerclere diqqet et.")
    elif xerc_faizi >=50 and xerc_faizi<=80:
        print("Budce normaldir")
    elif xerc_faizi <= 50:
        print("yaxsi qenaet edirsiz")

print ("ayin sonunda qalan pul meblegi:", qalan, "AZN")
print("Qenaet faizi: ",round(faiz,2) ,"%")