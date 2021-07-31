weather = input("오늘 날씨는 어때요")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")   
else:
    print("다 필요 없어요")   
      
temp = int(input("기온은 어때요?"))
if 30 <= temp:
    print("개 더우니까 집에있으세요")
elif 10 <= temp and temp < 30:
    print("나가셔도 괜찮을듯")   
elif 0 <= temp < 10:
    print("옷 입어라 추우니까")
else:
    print("빙하기")    