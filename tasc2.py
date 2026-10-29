tecrube = float(input("Tecrube illerinizi daxil edin: "))
bal = float(input("balinizi daxil edin(0-100): "))

if tecrube < 0 or bal<0 or bal>100:
    print("Xeta bas verdi.")
elif tecrube >= 2 and bal>=70:
    print(" novbeti merheleye devet olunur")
elif bal >= 90 :
    print("Guclu namizad")
else:
    print("namizad uygun deyil")
