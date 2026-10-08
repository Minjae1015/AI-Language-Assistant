import os
import json
import urllib.request
import urllib.parse

# 사용할 언어

languages = {
    "1": "Korean",
    "2": "English",
    "3": "Japanese",
    "4": "Chinese (Simplified)",
    "5": "French",
    "6": "German",
    "7": "Spanish"
}

lang_codes = {
    "Korean": "ko",
    "English": "en",
    "Japanese": "ja",
    "Chinese (Simplified)": "zh-CN",
    "French": "fr",
    "German": "de",
    "Spanish": "es"
}

# DeepL 언어 코드 

deepl_source = {
    "ko": "KO", "en": "EN", "ja": "JA",
    "zh-CN": "ZH", "fr": "FR", "de": "DE", "es": "ES"
}

deepl_target = {
    "ko": "KO", "en": "EN-US", "ja": "JA",
    "zh-CN": "ZH-HANS", "fr": "FR", "de": "DE", "es": "ES"
}

# DeepL API 키 

DEEPL_KEY = os.environ.get("DEEPL_KEY")

# 기록 저장

history = []
history_file = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "history.txt"
)


# API 번역

def translate_text(text, source, target):

    if not DEEPL_KEY:
        raise Exception("DEEPL_KEY is not set")

    data = urllib.parse.urlencode({
        "text": text,
        "source_lang": deepl_source[source],
        "target_lang": deepl_target[target]
    }).encode("utf-8")

    req = urllib.request.Request(
        "https://api-free.deepl.com/v2/translate",
        data=data,
        headers={"Authorization": "DeepL-Auth-Key " + DEEPL_KEY}
    )

    with urllib.request.urlopen(req, timeout=10) as response:
        result = json.loads(response.read().decode("utf-8"))

    return result["translations"][0]["text"]


# AI 문장 분석

def analyze_sentence(sentence):

    print(" \n \nAI Sentence Analysis")

    # 글자 수
    character_count = len(sentence)

    # 단어 수
    word_count = len(sentence.split())

    print("Characters :", character_count)
    print("Words :", word_count)

    # 문장 종류 분석
    if sentence.endswith("?"):
        print("Sentence type : Question")

    elif sentence.endswith("!"):
        print("Sentence type : Exclamation")

    else:
        print("Sentence type : Statement")

    # 긍정 / 부정 표현 분석
    positive_words = [
        "good", "great", "happy", "love", "like",
        "좋아", "좋은", "행복", "사랑"
    ]

    negative_words = [
        "bad", "sad", "hate", "angry",
        "싫어", "나쁜", "슬퍼", "화"
    ]

    positive_count = 0
    negative_count = 0

    lower_sentence = sentence.lower()

    for word in positive_words:
        if word in lower_sentence:
            positive_count += 1

    for word in negative_words:
        if word in lower_sentence:
            negative_count += 1

    if positive_count > negative_count:
        print("Tone : Positive")

    elif negative_count > positive_count:
        print("Tone : Negative")

    else:
        print("Tone : Neutral")

    # 문장 길이 분석
    if word_count <= 5:
        print("Sentence length : Short")

    elif word_count <= 15:
        print("Sentence length : Medium")

    else:
        print("Sentence length : Long")


while True:

    print(" \n \nAI Language Assistant")
    print("[1] Translate")
    print("[2] Translation history")
    print("[3] Saved history")
    print("[4] Delete history")
    print("[5] Exit")

    first_menu = input(" \n \nEnter a number: ")

    if first_menu == "2":

        print(" \n \nTranslation history:")

        if len(history) == 0:
            print("No history.")

        else:
            count = 1

            for original, result in history:
                print(f"\n[{count}]")
                print("Original :", original)
                print("Result :", result)
                count += 1

        input(" \n \nPress Enter to return to the menu")
        continue

    elif first_menu == "3":

        if os.path.exists(history_file):

            print(" \n \nSaved history:\n")

            with open(history_file, "r", encoding="utf-8") as file:
                print(file.read())

        else:
            print("No saved history")

        input(" \n \nPress Enter to return to the menu")
        continue

    elif first_menu == "4":

        if not os.path.exists(history_file):
            print("No history to delete")
            input(" \n \nPress Enter to return to the menu")
            continue

        print(" \n \nAre you sure you want to delete the history?")
        print("[1] Yes")
        print("[2] No")

        delete_choice = input("Enter a number: ")

        if delete_choice == "1":
            os.remove(history_file)
            history.clear()
            print("Translation history has been deleted")

        elif delete_choice == "2":
            print("Deletion cancelled")

        else:
            print("Please try again")

        input(" \n \nPress Enter to return to the menu")
        continue

    elif first_menu == "5":
        print("Exiting program")
        exit()

    elif first_menu != "1":
        print("Please try again")
        continue

    # 원본 언어
    while True:

        print(" \n \nSelect the source language")

        for num, name in languages.items():
            print(f"[{num}] {name}")

        source_choice = input("Enter a number: ")

        if source_choice in languages:
            break

        print("Please try again")

    # 번역할 언어
    while True:

        print(" \n \nSelect the target language")

        for num, name in languages.items():
            print(f"[{num}] {name}")

        target_choice = input("Enter a number: ")

        if target_choice in languages:
            break

        print("Please try again")

    # 같은 언어 선택 방지
    if source_choice == target_choice:
        print(" \n \nSource and target language are the same.")
        input(" \n \nPress Enter to return to the menu")
        continue

    # 문장 입력
    while True:

        text = input(" \n \n Enter the sentence to translate: ")

        if text.strip():
            break

        print(" \n \nPlease enter a sentence")

    # 언어 코드 매핑

    source = lang_codes[languages[source_choice]]
    target = lang_codes[languages[target_choice]]

    # 번역 실행 및 기록

    try:

        translated = translate_text(text, source, target)

        print(" \n-------------------------------- ") 
        print(" \nTranslation result:")
        print(translated)
        print(" \n-------------------------------- ")

        # 직접 만든 문장 분석
        analyze_sentence(translated)
        print(" \n-------------------------------- ")

        print(" \nBefore translation:")
        print("Characters :", len(text))
        print("Words :", len(text.split()))
        print(" \n-------------------------------- ")

        print(" \nAfter translation:")
        print("Characters :", len(translated))
        print("Words :", len(translated.split()))
        print(" \n-------------------------------- ")

        # 기록 저장
        history.append((text, translated))

        with open(history_file, "a", encoding="utf-8") as file:
            file.write("Original : " + text + "\n")
            file.write("Result : " + translated + "\n")
            file.write("-" * 30 + "\n")

    except Exception as e:

        if "429" in str(e) or "too many" in str(e).lower():
            print("Too many translation requests.")
            print("Please try again in a moment.")

        elif "456" in str(e):
            print("Monthly free quota (500,000 characters) used up.")

        elif "403" in str(e):
            print("Invalid API key. Check your DEEPL_KEY.")

        else:
            print("Translation error:")
            print(type(e).__name__)
            print(str(e)[:300])

    while True:

        print(" \n \n ")
        print("[1] Main menu")
        print("[2] Exit")

        menu = input(" \n \nEnter a number: ")

        if menu == "1":
            break

        elif menu == "2":
            print("Exiting program")
            exit()

        else:
            print("Please try again")
