# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 19:51:12 2024

@author: Student
"""

print("nhập 3 số a,b,c")
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
#phuong_trinh_bac_2 a*x^2+bx+c=0
if a==0:
    print("phương trình không phải là phương trình bậc 2")
else:
    print(f"phương trình bậc 2 là: {a}*x^2+{b}x+{c}=0")