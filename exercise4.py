print("Grades calculator")
math = int(input("math: "))
eng = int(input("eng; "))
phyc = int(input("phyc: "))
kisw = int(input("kisw: "))
hist = int(input("hist: "))


total = math + eng + phyc + kisw + hist
Average = total/5

if Average >=0 and Average <= 39:
    print("E")
elif Average >=39 and Average <=50:
    print("D")
elif Average >=50 and Average <= 60:
    print("C")
elif Average >=60 and Average <= 70:
    print("B")
elif Average >=70 and Average <= 100:
    print("A")
elif Average <= 0:
    print("Joker rudi class bana")
else:
    print("not normal")



