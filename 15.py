# 튜플 변경되지않는 목록 대신 속도가 빠름
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# 활용
name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)