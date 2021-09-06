# define function
def add(a, b):
    # 함수의 내용
    c = a + b
    return c

result = add(10, 20)
print(result)

"""
    def : definition 
    a, b : 매개 변수 
    c : 반환값
    10, 20 : 인자 [인수]

    인터프리터는 윗 줄부터 번역을 시작하지만,
    'def' 를 만나면 Skip 을 한다
    그런데 밑에서 새로운 함수를 만나게 되면 
    위 쪽으로 다시 함수를 찾으러 간다.
    함수를 찾을 때, 밑의 함수에 있던 값을 가지고 간다. 
    그리고 return 값을 가지고 와서 
    밑의 함수 값을 저장해 둔 변수에 값을 치환한다. 
    
    함수를 쓰는 이유
        1. 코드를 효율적으로 쓰기 위해
"""

