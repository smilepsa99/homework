from googletrans import Translator

translator = Translator()
sentence = input("책을 읽으며 인상 깊었던 구절을 적어주세요 : ")
detected = translator.detect(sentence)

lang1 = "en"
lang2 = "zh-CN"
result1 = translator.translate(sentence,lang1)
result2 = translator.translate(sentence,lang2)

print("\n==========번역결과==========\n")
print("입력어-",detected.lang,":",sentence)
print("번역어1-",lang1,":",result1.text)
print("번역어2-",lang2,":",result2.text,"\n")
print("============================")


#좀더 짧은 버전
# from googletrans import Translator

# translator = Translator()
# sentence = input("책을 읽으며 인상 깊었던 구절을 적어주세요 : ")

# result1 = translator.translate(sentence,"en")
# result2 = translator.translate(sentence,"zh-CN")

# print("\n==========번역결과==========\n")
# print("입력어-",result1.src,":",sentence)
# print("번역어1-",result1.dest,":",result1.text)
# print("번역어2-",result2.dest,":",result2.text)
# print("\n============================\n")