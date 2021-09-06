def func1():
    a = 1

func1()
# print(a)

"""
    지역 변수 (local variable) : 함수 안에서 만들어진 변수
        - 함수 안에서만 접근이 가능
        
    전역 변수 (global variable) : 함수 밖에서 만들어진 변수
        - 모든 지역에서 접근이 가능 (read-only)
        - 즉, 수정하는 것은 할 수 없다
"""

num = 10

def func2():
    global num # 전역변수 num 의 값 수정 허용 선언
    num += 1
    print(num)
