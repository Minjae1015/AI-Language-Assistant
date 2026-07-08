from deep_translator import GoogleTranslator

text = input("번역할 문장을 입력하세요")

translated = GoogleTranslator(source="auto", target="ko").translate(text)

print("번역 결과입니다:")

print(translated)