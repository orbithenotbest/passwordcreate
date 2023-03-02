import os
from strgen import StringGenerator as sifreUret

print("""
----------------------------------------------------------------------------------------------------
      Şifre Üretme
      
      
      #orbithebest


    NOT: Şifre üretmek için 'şf', 'şifre üret', 'şıfre uret', 'sifre üret', 'şifre'
    yazmanız yeterlidir. Ayrıca şifre ürettikten sonra tekrar şifre üretmek isterseniz
    yukarıda yazdığım şeylerden birini tekrardan yazmanız gerekmektedir.
    
    Keyifli kullanmalar!
----------------------------------------------------------------------------------------------------  
 """)

def sifre():
        kacsifre = input("Kaç şifre üretmek istiyorsunuz?")
        for i in range(int(kacsifre)):
            print(sifreUret(r"[\w]{24}"))

def chatbot_response(text):
    text = text.lower()
    if "şifre üret" in text or "şf" in text or "sifre üret" in text in text or "şıfre uret" in text or "şifre" in text:
         return sifre()
    


while True:
    user_input = input("Sen: ")
    if user_input.lower() == "kapat":
        break
    else:
        print("OrbitBOT: " , chatbot_response(user_input))