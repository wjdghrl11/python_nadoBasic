# 세트 집합 
# 중복 안됨, 순서 업음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java 파이썬 모두 할수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java 할수있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java할수있지만 python은 할줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

#jave를 잊었다
java.remove("김태호")
print(java)