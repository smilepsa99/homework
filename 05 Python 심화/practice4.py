import smtplib
from email.message import EmailMessage
import imghdr
import re

recvEmail = "smilepsa99@naver.com"
message = EmailMessage()
message.set_content("와우 개싱기")
message["Subject"] = "파이썬으로 메일보내기"
message["From"] = "smilepsa99@naver.com"
message["To"] = recvEmail

with open("C:\\Users\\smile\\OneDrive\\바탕 화면\\멋사 코딩\\homework\\05 Python 심화\\practice4_img.jpg","rb") as image:
    image_file = image.read()
image_type = imghdr.what("practice4_img",image_file)
message.add_attachment(image_file,maintype="image",subtype=image_type)

smtp = smtplib.SMTP("smtp.naver.com",587)
smtp.starttls()
smtp.login("smilepsa99@naver.com","699799sang!")

re_mail = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
if bool(re.match(re_mail,recvEmail)): #bool이란? https://wikidocs.net/17
    smtp.send_message(message)
    print("정상적으로 메일이 발송됐습니다.")
else:
    print("유효한 이메일 주소가 아닙니다.")

smtp.quit()

# !def를 사용할 경우!
# def recvEmail_check(x):
#     re_mail = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
#     if bool(re.match(re_mail,x)):
#         smtp.send_message(message)
#         print("정상적으로 메일이 발송됐습니다.")
#     else:
#         print("유효한 이메일 주소가 아닙니다.")

# recvEmail_check(recvEmail)
# smtp.quit()

