import os
from deep_translator import GoogleTranslator

# 사용할 언어
languages = {
    "1": "한국어",
    "2": "영어",
    "3": "일본어",
    "4": "중국어(간체)",
    "5": "프랑스어",
    "6": "독일어",
    "7": "스페인어",
    "8": "자동 감지"
}

lang_codes = {
    "한국어": "ko",
    "영어": "en",
    "일본어": "ja",
    "중국어(간체)": "zh-CN",
    "프랑스어": "fr",
    "독일어": "de",
    "스페인어": "es",
    "자동 감지": "auto"
}

# 기록 저장
history = []

while True:

    # 원본 언어
    while True:
        print(" \n \n 원본 언어를 선택하세요")
        for num, name in languages.items():
            print(f"[{num}] {name}")

        source_choice = input("번호 입력: ")

        if source_choice in languages:
            break

        print("다시 입력해주세요")

    # 2. 번역할 언어
    while True:
        print(" \n \n 번역할 언어를 선택하세요")
        for num, name in languages.items():
            if num == "8":
                continue
            print(f"[{num}] {name}")

        target_choice = input("번호 입력: ")

        if target_choice in languages and target_choice != "8":
            break

        print("다시 입력해주세요")

    # 3. 문장 입력
    while True:
        text = input(" \n \n 번역할 문장을 입력하세요: ")

        if text.strip():
            break

        print(" \n \n 문장을 입력해주세요")

    # 언어 코드 매핑
    source = lang_codes[languages[source_choice]]
    target = lang_codes[languages[target_choice]]

    # 번역 실행 및 기록
    try:
        translated = GoogleTranslator(source=source, target=target).translate(text)

        print(" \n \n 번역 결과:")
        print(translated)

        # 기록 저장
        history.append((text, translated))

    except:
        print("오류가 발생했습니다")

    # 4. 메뉴 선택 (홈)
    while True:
        print(" \n \n ")
        print("[1] 다시 번역")
        print("[2] 번역 기록")
        print("[3] 종료")

        menu = input(" \n \n 번호 입력: ")

        if menu == "1":
            break

        elif menu == "2":

            print(" \n \n 번역 기록입니다:")

            if len(history) == 0:
                print("기록이 없습니다.")

            else:
                count = 1
                for original, result in history:
                    print(f"\n[{count}]")
                    print("원본 :", original)
                    print("결과 :", result)
                    count += 1

            input(" \n \n 엔터를 누르면 메뉴로 돌아갑니다")

        elif menu == "3":
            print("프로그램 종료")
            exit()

        else:
            print("다시 입력해주세요")