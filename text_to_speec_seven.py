import speech_recognition as sr    #ses tanıma motoru
import pyaudio                     #bu kütüphaneyi python versiyonunuza göre 
from gtts import gTTS              #yazıyı sese çevirmek için gTTS kütüphanesi bize gerekiyor bu kütüphane terminale pip install gTTS yazarak indirilir
from playsound import playsound    #playsound'un 1.2.2 versiyonunu indirmeniz gerekiyor
import os
from datetime import datetime         #standart olarak python içinde bu modül gelmektedir
import time                           #standart olarak python içinde bu modül gelmektedir
import webbrowser     #standart olara python içinde webbrowser modülü gelmektedir


r=sr.Recognizer()              #sr recognizer sınıfını yazılımımıza ekliyoruz bu sınıf bizim mikrofondan dinleme yapmamızı sağlayan methodları barındırıyor



def record(ask=False):
    with sr.Microphone() as source:    #mikrofonu açıp mikrofondan elde edilen veriyi source değişkenine atamamızı sağlayan komut
        if ask:
            print(ask)
        audio=r.listen(source)         #source'den gelen ses verisi bir değişkene atanıyor
        voice=""

        try:
            voice= r.recognize_google(audio,language="tr")     #soruce'den gelen ses verisi google'nin sesi yazıya dönüştürme motoruna veriliyor ve yazıya çevriliyor

        except sr.UnknownValueError:
            print("Asistan: Anlayamadım")
        except sr.RequestError:
            print("sistem çalışmıyor")
        return voice
    

def speak(string):
    tts=gTTS(text=string,lang="tr")     #fonskiyonumuz parametre olarak bir string alıyor ve bu string bu satırda ki fonksiyon ile sese çeviriyor
    file="answer.mp3"                   #sese çevrilen yazıyı oynatabilmemiz için kaydetmemiz ve isimlendirmemiz lazım burada isimlendirme yapılıyor
    tts.save(file)                      #gTTS'in methodlarından birini kullanarak dosyayı kod dizinimize kaydediyoruz
    playsound(file)                     # Playsound fonskiyonu sesi oynatmamızı sağlıyor. Cevap bu fonksiyon ile veriliyor
    os.remove(file)                     # os standart bir python kütüphanesi bu fonksiyon ile oynatılan ve artık işimize yaramayan ses dosyasını siliyoruz


def response(voice):                            #bu fonskiyon record fonskiyonundan döndürdüğümüz komuta göre ne yapılmasını gerektiğini söyleyen komutları içeriyor

    if "merhaba" in voice:                      #eğer sisteme merhaba dersek bize speak fonksiyonu ile "sana da merhaba" cevabını veriyor
        speak("sana da merhaba Ömer")
    if "kapan" in voice:
        speak("kapanıyorum iyi günler")
        exit()

    if "hangi gündeyiz" in voice:               #time kütüphanesini kullanarak bize hangi günde olduğumu söylüyor

        today=time.strftime("%A")
        print(today)
        if today=="Thursday":
            today="perşembe"
        speak(today)
    if "saat kaç" in voice:                    #datetime modülünü kullanarak bize saatin kaç olduğunu söylüyor

        clock=datetime.now().strftime("%H:%M")
        speak(clock)
    if "google'da ara" in voice:              #webbrowser modülünü kullanarak istediğimiz sitede gezinmemizi sağlıyor
        speak("ne aramamı istersin")
        playsound("dinleme.mp3")
        search=record()
        playsound("kapan.mp3")
        url="https://www.google.com/search?q=" + search
        webbrowser.get().open(url)
        speak(search+ " " + "için google'da bunları buldum")

    if "notumu hesaplar mısın" in voice:
        speak("Tabiki hesaplarım ilk sınav notunu söyleyebilir misin ?")
        not1=record()
        print(not1)
        speak("İkinci sınav notunu söyler misin ?")
        not2=record()

        not1=int(not1)
        not2=int(not2)
        ort=(not1+not2)/2
        speak("Sınav ortalamanız "+ str(ort))


    speak("Başka bir isteğin var mı ?")
    playsound("dinleme.mp3")

speak("Sesli asistana hoşgeldiniz")
i=0
while True:
    if i==0:
        playsound("dinleme.mp3")
        i +=1
    voice=record()
    if voice !='':

        
        voice=voice.lower()
        playsound("kapan.mp3")
        print(voice) 
        response(voice)
        
