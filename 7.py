from random import *

print(random()) # 0.0~1.0 미만의 임의의 값
print(random() * 10) # 0.0~10.0 미만의 임의의 값
print(int(random() * 10)) # 0~10 이하의 임의의 값
print(int(random() * 10) + 1)  # 1~10 이하의 임의의 값

print(int(random() * 45) + 1) # 1~45 이하의 임의의 값

print(randrange(1,46)) # 1~46 미만의 임의의 값
print(randint(1,45)) # 1~45 이하의 임의의 값 생성

from random import *
day = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월" + str(day) + "일로 선정되었습니다.")