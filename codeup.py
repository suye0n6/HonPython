#1901
n = int(input()) #n 입력

def f(n): #재귀함수 실행
    if n != 1: #n이 1이 아닐 때
        f(n-1) #n-1 하면서 순서대로 나열되도록 수 만들기 예시로 n이 3일때는 3-1으로 2를 생성
    print(n)#한개씩 출력
f(n)

#1902
n = int(input()) #n 입력

def f(n): #재귀실행
    if n == 1: #n이 1이면
        print(n) #1바로 출력
    else: #다른 자연수일때
        print(n) #n출력후
        f(n-1)#n-1 로 역순 출력
f(n)
#1904
n, m = input().split() #두 자연수 입력
n = int(n) #int 형 변환 
m = int(m)

def f(n,m): 
    if n>m:
        return 0
    elif m%2:
        f(n,m-1)
        print(m,end= " ")
    elif not m%2:
        f(n,m-1)
f(n,m)

