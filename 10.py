python = "Python is Amazing"
print(python.lower()) # 올 소문자
print(python.upper()) # 올 대문자
print(python[0].isupper()) # 0번째 대문자
print(python[0].islower()) # 0번째 소문자
print(len(python)) # 문자의 길이를 출력해준다
print(python.replace("Python", "Java")) # 변경해준다

index = python.index("n") 
print(index)
# 파이썬이란 변수에서 괄호안 문자를 위치를알려준다
index = python.index("n", index + 1) 
print(index)
# 두번째를 찾아준다

print(python.find("Java")) # 없을때 -1 반환
print(python.index("Java")) # 없을때 에러
print(python.count("n"))