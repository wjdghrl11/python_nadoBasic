# while
custmer = "토르"
index = 5
while index >= 1:
    print("{0}님 커피가 준비 되었습니다. {1}번 남았어요.".format(custmer, index))
    index -= 1
    if index == 0:
        print("커피 품절입니다.")

# 무한 루프
customer = "아이언맨"
index = 1
while True:
    print("{0}님 커피가 준비 되었습니다. 호출{1}회".format(customer, index))
    index += 1
