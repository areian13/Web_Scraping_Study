import requests
res = requests.get("http://google.com")
# res = requests.get("http://nadocoding.tistory.com")
# res = requests.get("https://www.acmicpc.net")
print("응답코드: ", res.status_code)

# if res.status_code == requests.codes.ok:
#     print("정삽입니다")
# else:
#     print(f"문제가 생겼습니다. [에러코드: {res.status_code}]")

res.raise_for_status() # 200이 아니면 오류를 터뜨리는 함수
print("웹 스크래핑을 진행합니다")

print(len(res.text))
print(res.text)

with open("../mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)