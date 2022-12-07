import sys
import webbrowser
import pyttsx3
import pyaudio
from fuzzywuzzy import fuzz
import speech_recognition as sr
import dictionaryOfCommands as lists


class Talk:
    def __init__(self):
        self.peopleTalk = self.talk()

    def talk(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Говорите")
            r.pause_threshold = 0.5
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            words = r.recognize_google(audio, language="ru-RU").lower()
            print("Вы сказали: " + words)
            # Speech(words)
        except sr.UnknownValueError:
            Speech("Я вас не поняла")
            words = self.talk()
        return str(words)


class Speech:
    def __init__(self, words):
        self.speech(words)

    def speech(self, words):
        engine = pyttsx3.init()
        engine.setProperty("voice", "ru")
        engine.say(words)
        engine.runAndWait()


class Bot:
    def __init__(self, word):
        self.makeSomething(self.comparison(word))

    def comparison(self, words):
        maxes = [(k, max([fuzz.ratio(words, w) for w in lst])) for k, lst in lists.my_dict.items()]
        ali_words = max(maxes, key=lambda x: x[1])
        return "pass" if ali_words[1] < 51 else ali_words[0]

    def makeSomething(self, word):
        match word:
            case "vk": self.vk()
            case "youtube": self.youTube()
            case "translate": self.translator()
            case "radio": self.radio()
            case "stop": self.stop()
            case _: Speech("Я пока этого не умею")

    def stop(self):
        Speech("Пока")
        sys.exit()

    def radio(self):
        Speech("Уже открываю")
        url = 'https://radio.yandex.ru/mood/energetic?from=alice&mob=0&play=1'
        # https://radio.yandex.ru/mood/relaxed?from=alice&mob=0&play=1
        # https://music.yandex.ru/users/yamusic-daily/playlists/128579782?from=alice&mob=0&play=1 плейлист дня
        # https://radio.yandex.ru/mood/beautiful?from=alice&mob=0&play=1

        webbrowser.open(url)

    def translator(self):
        Speech("Уже открываю")
        url = 'https://translate.yandex.ru/'
        webbrowser.open(url)

    def vk(self):
        Speech("Уже открываю")
        url = 'https://vk.com'
        webbrowser.open(url)

    def youTube(self):
        Speech("Уже открываю")
        url = 'https://www.youtube.com/'
        webbrowser.open(url)


while True:
    people = Talk()
    Bot(people.peopleTalk)
