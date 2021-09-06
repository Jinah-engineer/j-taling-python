# 파일 열기 모드
# r : read mode
# but 존재하지 않는 파일명을 쓰면 error 발생

f = open("test.txt", "r", encoding='utf-8')
# result = f.readline()
# result = f.read()
result = f.readlines() # list
f.close()


print(result)