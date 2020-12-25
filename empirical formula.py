import math
def Molar(c,h,o):
    Mm_O=15.994
    Mm_H=1.007
    Mm_C=12.011
    nC=c*(1/Mm_C)
    nO=o*(1/Mm_O)
    nH=h*(1/Mm_H)
    nC=round(nC,3)
    nO=round(nO,3)
    nH=round(nH,3)
    list=[nC,nH,nO]
    lst=[]

    lst.append((round(nC/min(list),3)))
    lst.append((round(nH/min(list),3)))
    lst.append((round(nO/min(list),3)))
    return lst

def main():
    while(1):
        print("enter percentage composition of the compound in terms of its constituent elements (carbon, hydrogen, oxygen) of the total must be 100%")
        C=float(input("enter the percentage constituents of a compound that contains carbon (C):"))
        H=float(input("enter the percentage constituents of a compound that contains Hydrogen (H):"))
        O=float(input("enter the percentage constituents of a compound that contains oxygen (O):"))
        t=float(100)
        if((C+H+O)==t):
            lst3 = Molar(C, H, O)
            s=lst3[1]-math.floor(lst3[1])
            if s<0.75:
                lst3[1]=math.floor(lst3[1])
            else:
                lst3[1] = math.ceil(lst3[1])


            print("C" + str(math.ceil(lst3[0])) + "H" + str(lst3[1]) + "O")
            print("Thanks for using this app!")
            break
        else:
            print("The total of all percentages must be 100%")




if __name__=="__main__":
    main()