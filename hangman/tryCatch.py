# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 11:34:56 2020

@author: palar
"""
def normalize(numbers):
    max_number = max(numbers)
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
    return numbers  

def normalizeD(numbers):
    max_number = max(numbers)
    assert(max_number != 0), "Cannot divide by 0"
    for i in range(len(numbers)):
        numbers[i]  /= float(max_number)
        assert(0.0 <= numbers[i] <= 1.0), "output not between 0 and 1"
    return numbers 

print(normalize([1,2,3,4]))
# ============ASSERT=================================================================
# def avg(grades):
#     assert not len(grades)==0, 'No grades data, wey.'
#     return sum(grades)/len(grades)
# print(avg([]))
# ============Assert=================================================================
# =============================EXCEPTION_ZERODIVISIONERROR================================================
# def fancy_divide(list_of_numbers, index):
#    denom = list_of_numbers[index]
#    return [simple_divide(item, denom) for item in list_of_numbers]
# 
# 
# def simple_divide(item, denom):
#    try:
#        return item / denom
#    except ZeroDivisionError:
#        return 0
# 
# print(fancy_divide([0,2,4],0))
# 
# =============================EXCEPTION_ZERODIVISIONERROR================================================
# =============================================================================
# # =============================FIRST_ONE================================================
# # def fancy_divide(numbers,index):
# #     try:
# #         denom = numbers[index]
# #         for i in range(len(numbers)):
# #             numbers[i] /= denom
# #     except IndexError:
# #         print("-1")
# #     else:
# #         print("1")
# #     finally:
# #         print("0")
# #         
# # =============================FIRST_ONE================================================
# # =============================SECOND_ONE================================================
# # def fancy_divide(numbers, index):
# #     try:
# #         denom = numbers[index]
# #         for i in range(len(numbers)):
# #             numbers[i] /= denom
# #     except IndexError:
# #         fancy_divide(numbers, len(numbers) - 1)
# #     except ZeroDivisionError:
# #         print("-2")
# #     else:
# #         print("1")
# #     finally:
# #         print("0")
# # =============================SECOND_ONE================================================
# # =============================THIRD_ONE================================================
# # def fancy_divide(numbers, index):
# #     try:
# #         try:
# #             denom = numbers[index]
# #             for i in range(len(numbers)):
# #                 numbers[i] /= denom
# #         except IndexError:
# #             fancy_divide(numbers, len(numbers) - 1)
# #         else:
# #             print("1")
# #         finally:
# #             print("0")
# #     except ZeroDivisionError:
# #         print("-2")
# # =============================THIRD_ONE================================================
# # =============================FOURTH_ONE================================================
# # def fancy_divide(list_of_numbers, index):
# #     try:
# #         try:
# #             raise Exception("0")
# #         finally:
# #             denom = list_of_numbers[index]
# #             for i in range(len(list_of_numbers)):
# #                 list_of_numbers[i] /= denom
# #     except Exception as ex:
# #         print(ex)
# # =============================FOURTH_ONE================================================
# # =============================FIFTH_ONE================================================
# # def fancy_divide(list_of_numbers, index):
# #     try:
# #         try:
# #             denom = list_of_numbers[index]
# #             for i in range(len(list_of_numbers)):
# #                 list_of_numbers[i] /= denom
# #         finally:
# #             raise Exception("0")
# #     except Exception as ex:
# #         print(ex)
# # print(fancy_divide([0,2,4],0))
# # =============================FIFTH_ONE================================================
# 
# =============================================================================
# =========================GET_STATS====================================================
# def get_stats(class_list):
#     new_stats=[]
#     for elt in class_list:
#         new_stats.append([elt[0],elt[1], avg(elt[1])])
# def avg(grades):
#     try:
#         return sum(grades)/len(grades)
#     except ZeroDivisionError:
#         print("no grades data")
#         return 0.0
# 
# test_grades=[['peter','parker'],[10.0,5.0,85.0]],[['bruce','wayne'],[10.0,8.0,74.0]],[['captain','america'],[8.0,10.0,96.0]],[['deadpool'],[]]
# =========================GET_STATS====================================================
# ================================GET_RATIOS=============================================
# def get_ratios(L1,L2):
#     """
#     Assumes: L1 and L2 are lists of equals length of numbers
#     Returns: a list containing  L1[i]/L2[i]
#     """
#     ratios=[]
#     for index in range(len(L1)):
#         try:
#             ratios.append(L1[index]/float(L2[index]))
#         except ZeroDivisionError:
#             ratios.append(float('NaN'))
#         except:
#             raise ValueError('get_ratios called with bad arg')
#         return ratios
# ==================================GET_RATIOS===========================================
# =========================DIFFERENT EXCEPTIONS====================================================
# try:
#     a=int(input("Tell me one number"))
#     b=int(input("Tell me another number"))
#     print(a/b)
#     print("Okay")
# except ValueError:
#     print("ValueError")
# except ZeroDivisionError:
#     print("ZeroDivision")
# except: #else:
#     print("Error no cashado")
# ==========================DIFFERENT EXCEPTIONS===================================================
#finaly:
# =============================================================================
# try:
#     a=int(input("Tell me one number"))
#     b=int(input("Tell me another number"))
#     print(a/b)
#     print("Okay")
# except:
#     print("Bug")
#     
# =============================================================================
#print("xd")