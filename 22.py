for waiting_no in [0,1,2,3,4]:
    print("대기번호 : {0}".format(waiting_no))

    # for문
for no_1 in [0,1,2,3,4]:
    print("순번대기 : {0}".format(no_1))

# randrange() 함수를 사용한 for문
for no_1 in range(5):
    print("순번대기 : {0}".format(no_1))

starbucks = ["아이먼맨", "토르", "그루트"]
for customer in starbucks:
    print("{0}님 주문하신 커피가 준비되었습니다.".format(customer))