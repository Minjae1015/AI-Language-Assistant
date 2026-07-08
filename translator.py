from deep_translator import GoogleTranslator

text = input("번역할 문장을 입력하세요: ")

print("\n사용 가능한 언어")
print("ko = 한국어")
print("en = 영어")
print("ja = 일본어")
print("zh-CN = 중국어(간체)")
print("fr = 프랑스어")
print("de = 독일어")
print("es = 스페인어")

source = input("원본 언어를 입력하세요 (자동 감지는 auto): ")
target = input("번역할 언어를 입력하세요: ")

translated = GoogleTranslator(
    source=source,
    target=target
).translate(text)

print("번역 결과입니다:")

print(translated)