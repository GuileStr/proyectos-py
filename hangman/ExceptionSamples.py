# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 11:45:23 2020

@author: palar
"""
try:
    a=int(input("Tell me a number"))
    b=int(input("Tell me another number"))
    print(a/b)
    print("okay")
except:
    print("Fallo en la matrix")
print("salimos, papu")
# ==============================TRY/EXCEPT TO GET AN INTEGER=======================================
# while True:
#     try:
#         n = input("Please enter an integer: ")
#         n=int(n)
#         break
#     except ValueError:
#         print("Input not an integer; try again")
# print("Correct input of an integer")
# ==============================TRY/EXCEPT TO GET AN INTEGER===============================================
# ==============================TRY/EXCEPT TO OPEN A FILE AN SAVE GRADES===============================================
# data=[]
# file_name=input("Provide a name of a file of data")
# try:
#     fh = open(file_name,'r')
# except IOError:
#     print("cannot open", file_name)
# else:
#     for new in fh:
#         if new != '\n':
#             addIt = new[:-1].split(',')
#             data.append(addIt)
# finally:
#     fh.close()
#     
# gradesData=[]
# if data:
#     for student in data:
#         try:
#             name = student[0:-1]
#             grades= int(student[-1])
#             gradesData.append([name,grades])
#         except ValueError:
#             gradesData.append([student[:],[]])
# =============================================================================
