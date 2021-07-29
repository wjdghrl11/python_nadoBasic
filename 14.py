# 사전
cabinet = {3:"유재석", 100:"김태호"} # 키 3,100 쓰고있는사람 유재석씨 김태호
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3)) # 이렇게도 가능
# print(cabinet[5]) # 밑에 hi를 출력안하고 5에 해당하는 자료가없어서 프로그램종료
# print(cabinet.get(5))
# 대괄호로 값을 가져올때 값이없는경우에는 오류출력후 프로그램종류
# get을 이용했을때는 none이라고 출력하고 프로그램을 이어나갈수있다.
print(cabinet.get(5, "사용가능"))
print("hi")

print(3 in cabinet) # 존재하면 True
print(5 in cabinet) # 존재하지않아서 False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)