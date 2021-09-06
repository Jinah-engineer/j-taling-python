import random

ans = random.randint(1, 100)
print('Start up and down game ! ')

cnt = 0

while True:
    input1 = int(input('숫자 입력 >>> '))
    cnt += 1
    if input1 == ans:
        print('It is correct ! ')
        break
    elif input1 > ans:
        print('Down!')
    elif input1 < ans:
        print('Up!')

print('{}회 만에 정답을 맞히셨습니다.'.format(cnt))