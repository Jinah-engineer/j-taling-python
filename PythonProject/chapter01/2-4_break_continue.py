num = 0
while True: # 조건무를 무조건 만족시킨다. 무한 loop
    num += 1
    if num % 2 == 1:
        continue
    print(num)
    if num == 20:
        break # 반복문을 강제 탈출시킴.

