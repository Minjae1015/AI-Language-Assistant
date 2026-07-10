from deep_translator import GoogleTranslator

#언어 목록
languages = {
    "1": "한국어",
    "2": "영어",
    "3": "일본어",
    "4": "중국어(간체)",
    "5": "프랑스어",
    "6": "독일어",
    "7": "스페인어"
}

lang_codes = {
    "한국어": "ko",
    "영어": "en",
    "일본어": "ja",
    "중국어(간체)": "zh-CN",
    "프랑스어": "fr",
    "독일어": "de",
    "스페인어": "es"
}

#원본 언어 선택
print("\n \n 원본 언어를 선택하세요.")
for num, name in languages.items():
    print(f"[{num}] {name}")
print("[8] 자동 감지")

source_choice = input("입력 (1~8): ")

#결과 언어 선택
print("\n \n번역할 언어를 선택하세요.")
for num, name in languages.items():
    print(f"[{num}] {name}")

target_choice = input("입력 (1~7): ")

#번역 문장 입력
text = input("\n \n 번역할 문장을 입력하세요:")

if source_choice == "8":
    source = "auto"
else:
    source = lang_codes[languages[source_choice]]

target = lang_codes[languages[target_choice]]

#번역 결과
try:
    translated = GoogleTranslator(
        source=source,
        target=target
    ).translate(text)

    print("\n \n 번역 결과입니다:")
    print(translated)

#오류
except Exception:
    print("\n \n 번역 중 오류가 발생했습니다")
