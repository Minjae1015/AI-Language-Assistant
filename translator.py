import os
import json
import torch
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer
from huggingface_hub import login
  
login(token=os.getenv("HF_TOKEN"))
  
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
      "Chinese (Simplified)": "zh",  
      "French": "fr",
      "German": "de",
      "Spanish": "es"
}   
  
# AI 모델 설정 
MODEL_NAME = "facebook/m2m100_418M"
tokenizer = M2M100Tokenizer.from_pretrained(MODEL_NAME)
model = M2M100ForConditionalGeneration.from_pretrained(MODEL_NAME)
  
# 기록 저장
history = []
history_file = os.path.join(
      os.path.dirname(os.path.abspath(__file__)),
      "history.txt"
)   
  
# AI 번역 함수 
def translate_text(text, source, target):
    """
    Translates text between any supported languages using M2M100.
    """
    tokenizer.src_lang = source
    
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=1024)
    with torch.no_grad():
        generated_tokens = model.generate(
            **inputs,
            forced_bos_token_id=tokenizer.get_lang_id(target),
            max_new_tokens=1024
        )   
    translated_text = tokenizer.decode(generated_tokens[0], skip_special_tokens=True)
    return translated_text

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

    # 긍정, 부정 표현 분석
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

    if source_choice == target_choice:
        print(" \n \nSource and target language are the same.")
        input(" \n \nPress Enter to return to the menu")
        continue

    # 파일에서 긴 텍스트 읽기 
    input_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "input.txt"
    )

    if not os.path.exists(input_file_path):
        print(" \n \nError: 'input.txt' not found!")
        print("Please create an 'input.txt' file in the same folder and put your text inside it.")
        input(" \n \nPress Enter to return to the menu")
        continue

    with open(input_file_path, "r", encoding="utf-8") as f:
        text = f.read().strip()

    if not text:
        print(" \n \n'input.txt' is empty! Please add some text to translate.")
        input(" \n \nPress Enter to return to the menu")
        continue

    print(f"Loaded {len(text)} characters from input.txt successfully!")

    source = lang_codes[languages[source_choice]]
    target = lang_codes[languages[target_choice]]

    print(" \nTranslating... please wait (local AI is processing on CPU)...")

    # 번역 실행 및 기록 
    try:
        paragraphs = text.split("\n")
        translated_paragraphs = []

        for p in paragraphs:
            if p.strip() == "":
                translated_paragraphs.append("")
                continue
            p_translated = translate_text(p, source, target)
            translated_paragraphs.append(p_translated)

        translated = "\n".join(translated_paragraphs)

        print(" \n-------------------------------- ") 
        print(" \nTranslation result:")
        print(translated)
        print(" \n-------------------------------- ")

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

        history.append((text, translated))

        with open(history_file, "a", encoding="utf-8") as file:
            file.write("Original : " + text + "\n")
            file.write("Result : " + translated + "\n")
            file.write("-" * 30 + "\n")

    except Exception as e:
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
