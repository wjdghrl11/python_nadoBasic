# 컨티뉴 브레이크
absent = [2, 5] # 결석
no_book = [7] # 책 안가져옴
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 없다 {0}은 교무실로".format(student))
        break
    print("{0}야 책읽어".format(student))