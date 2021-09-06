"""
    파일 입출력 함수
"""
"""
    기본 입출력 함수 : 출력의 대상이 모니터(print) , 입력의 대상이 키보드 (input)
    
    파일 입출력 함수 : 출력의 대상이 모니터가 아닌 '파일' 
        - write() = 기록
        - read() = 읽어들이기 (파일로부터)
"""

print("hello")
print('world')
print('python')

# 내가 기록할 파일
# w = write mode
# w 모드는 파일 존재하지 않으면, 파일을 새로 생성한다
# 파일의 내용을 모두 지운 후, 파일을 연다.

# a mode : 더해서 쓰기 모드
# 파일이 존재하지 않으면, 파일을 새로 생성한다.
# 파일의 내용을 모두 유지한 후, 파일을 연다.

# 경로는 자유롭게 설정 가능
# doc. ppt. xls. 파일도 생성 가능

f = open('test.txt', 'w')
f.write('hello\n')
f.write('world\n')
f.write('python\n')
f.close() # 파일 닫아주기