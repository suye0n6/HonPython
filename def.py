#1548

n = int(input())

def grade(n):
  if n >=90 :
    print("A")
  elif n >= 80:
    print("B")
  elif n >= 70:
    print("C")
  elif n >= 60:
    print("D")
  elif n < 60:
    print("F")

grade(n)

#1549
n = int(input())

def f(n):
  if n>=0:
    print(n)
  elif n<0:
    print(-n)

f(n)

#1551
n=int(input())
number = map(int,input().split())
number = list(number)
k = int(input())

def lenf(k):
    flag=Flase
    for idx in range(len(number)):
       if number[idx] == k:
          print(idx+1)
          flag=True
          break
       if not flag:
        print(-1)

f(k)

