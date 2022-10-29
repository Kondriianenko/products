print("fuck you")
a = str(input())
b = str(input())
if a.isalpha() == True and b.isalpha() == True:
    a_list=list(a)
    b_list=list(b)
    aso=sorted(a_list)
    bso=sorted(b_list)
if aso==bso:
    print("YES")
else:
    print("NO")

