
phoneList = []

f = open("./phone_book.txt", "r")
data = f.readlines()
for i in data:
    print(i.strip()) # 끝에 있는 개행 지우기 = strip() -- 양 끝에 있는 공백, 개행문자를 지워줌
    i.split(",") # split() : "," 를 기준으로 값을 나눈 후 리스트형으로 반환
    phoneList.append({"name": i[0], "number": i[1]})

numOfData = len(phoneList)

def inputData():
    name = input('이름 입력 : ')
    number = input('번호 입력 : ')
    phoneList.append({'name': name, 'number': number})

    # 전화번호부 생성
    f = open("./phone_book.txt", "a")
    f.write(name + "," + number + "\n")
    f.close()

    global numOfData
    numOfData += 1

while True:
    print('='*50)
    print('현재 데이터 개수 : {}개'.format(numOfData))
    print("1. 전화번호 추가")
    print("2. 전화번호 검색")
    print("3. 전화번호 삭제")
    print("4. 전화번호 전체 출력")
    print('='*50)

    menu = int(input("선택 >>> "))


    if menu == 1:
        inputData()


    elif menu == 2:
        search_name = input("검색할 이름 입력 >>> ")

        is_find = False

        for data in phoneList:
            if data["name"] == search_name:
                print('-' * 30)
                print("이름 : ", data["name"])
                print("번호 : ", data["number"])
                print('-' * 30)
                is_find = True

        if is_find == False: # 검색에 실패했다면
            print('찾는 이름이 없습니다.')


    elif menu == 3:
        delete_name = input("삭제할 이름 입력 >>> ")

        is_find = False

        for data in phoneList:
            if data["name"] == delete_name:
                phoneList.remove(data)
                numOfData -= 1
                is_find = True

        if is_find == False:  # 검색에 실패했다면
            print('찾는 이름이 없습니다.')


    elif menu == 4:
        for data in phoneList:
            print('-' * 30)
            print(data["name"])
            print(data["number"])
            print('-' * 30)
    elif menu == 5:
        print('종료되었습니다.')
        break
    else:
        print("올바른 선택이 아닙니다.")