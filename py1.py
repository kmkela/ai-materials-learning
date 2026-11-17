# print("hello world")
# num1=3
# num2=10
# total=num1+num2
# print(num1+num2)
# a=333
# print(a)
# a=111
# print(a)
# input("nihao")
# height=float(input("请输入你的身高："))
# weight=float(input("write your weight:"))
# total=height+weight
# print("总:%f"%total)
# print("six\tsix")
# print("sixs\nix")
# print(r"sd\rsds")
# print("sixs\\rix")
# a=str("sa")
# type(a)
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(str(j)+"x"+str(i)+"="+str(j*i)+"\t",end="")
#     print("")
# print("a")
# print("a",end="")
# for i in range(1,3):
#     for j in range(1,i+1):
#         print(str(j),"x"+str(i),"=",str(j*i),"\t",end="")
# print("hello","world")
# print("hello"+"world")
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(str(j)+"x"+str(i)+"="+str(j*i)+"\t",end="")
#     print("")
# for i in range(4):
#     print(i)
# for i in range(4):
#     print("***猜第{}个数***".format(i+1))
# x=42
# print(f"x={x}")
# for i in range(4):
#     print(f"***猜第{i+1}个数***")
# from random import randint
# x=randint(0,100)
# print(x)
# from random import randint
# point=randint(1,6)
# for i in range(1,4):
#     guess = int(input("请输入你要猜测的数字："))
#     if guess==point:
#         print("猜测正确")
#         break
#     elif guess>point:
#         print("猜测错误，数值偏大")
#         continue
#     elif guess<point:
#         print("猜测错误，数值偏小")
#         continue
# else:
#     print("您的机会已经用完")
# import random
# help(random)
# for i in range(1,20):
#     if i%2==0:
#         print(i,end=" ")
#     else:
#         continue
#第3章 第一题
# per_num=int(input("输入乘坐人数："))
# sta_num=int(input("输入乘坐站数："))
# if 1<=sta_num<=4 and per_num>0:
#     d=per_num*3
#     print(f"总金额：{d}")
# elif 5<=sta_num<=9 and per_num>0:
#     d=per_num*4
#     print(f"总金额：{d}")
# elif 10<=sta_num and per_num>0:
#     d=per_num*5
#     print(f"总金额：{d}")
# else:
#     print("error")
#第二题
# x=float(input("请输入横坐标："))
# y=float(input("请输入纵坐标："))
# if x>0 and y>0:
#     print("坐标在第一象限")
# elif x<0 and y<0:
#     print("坐标在第三象限")
# elif x<0 and y>0:
#     print("坐标在第二象限")
# elif x>0 and y<0:
#     print("坐标在第四象限")
# else:
#     print("坐标在坐标轴上")
#第三题(未完成）
# a=int(input("Enter a number:"))
# b=a//1000%10
# print(b)
#第四题
# hello_world=123
# print(hello_world)
#5题
# a=input("Enter a str")
# digits=""
# for ch in a:
#     if "0" <= ch <= "9":
#         digits+=ch
#     else:
#         pass
# n=int(digits)
# print(n)
#6题
# for i in range(100,1000):
#     a=i%10
#     b=i//10%10
#     c=i//100%10
#     if a**3+b**3+c**3==i:
#         print(i,end=" ")
#     else:
#         continue
#8题
# for i in range(1,31):
#     a=100000*i
#     b=0.01*2**i
#     # print(f"第{i}天mode:{b}")
#     # print(f"第{i}天fude:{a}")
#     if a<=b:
#         print(f"陌生人在第{i}天超过富豪",f"陌生人的钱数是{b}",f"富豪的钱数是{a}",sep="\n")
#         break
#     elif a>b:
#         continue

# list=[1,2.3]
# list.clear()
# print(list)

