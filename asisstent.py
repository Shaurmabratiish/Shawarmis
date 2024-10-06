
import speech_recognition as sr
import os
import sys
import webbrowser
import gtts 
import gtts
import pygame
from pygame import mixer
from playsound import playsound 
import subprocess
import time
from threading import Thread
import random
import asyncio
import keyboard
from datetime import datetime
pygame.mixer.init()
pygame.display.init() 
comamnds_check = True
playlist_list = []
bot_appeal = "Господин"
bot_name = "Виверс"
running = False
bot_voice = True
playlist_check = False
last_load_music = ""
bot_repeat_music = 0
volume_sound = 0.2
playlist_already_ready = 0
is_track = False

config_directory = "" + os.path.dirname(__file__) + "/config"
config_boss_file = config_directory + "/config_data.txt"
music_directory = config_directory + "/music"
programms_direcotry = config_directory + "/programms"
config_programms = programms_direcotry + "/config_programms.txt"
browser_directory = config_directory + "/browser"
config_browser = browser_directory + "/config_browser.txt"
def config_string_values():
    with open(config_boss_file, 'w+') as f:
        f.write("voiceAssistentSaying=1\n")
        f.write("botName=Рокси\n")
        f.write("botAppeal=Никита\n")
        f.write("repeatMusic=0\n")
        f.write("volumeSound=0.2\n")
        f.close()
        print("as")
def get_config_data():
    global bot_appeal
    global bot_name
    global bot_voice
    global bot_repeat_music
    global volume_sound
    file1 = open(config_boss_file, "r")
    lines = file1.readlines()
    for z in lines:
        splittext = z.split("=")
        print(f"Переменная: {splittext[0]}\n Значение: {splittext[1]}")
        if splittext[0] == "botName":
            bot_name = splittext[1]
        elif splittext[0] == "voiceAssistentSaying":
            bot_voice = int(splittext[1])
        elif splittext[0] == "botAppeal":
            bot_appeal = splittext[1]
        elif splittext[0] == "repeatMusic":
            bot_repeat_music = int(splittext[1])
        elif splittext[0] == "volumeSound":
            volume_sound = float(splittext[1])


def start_settings_code():
    name_File = os.path.dirname(__file__)
    list_ = os.listdir(name_File)
    print("start settings function")
    for z in list_:
        print(name_File + f"/{z}")
        if ".mp3" in z:
            os.remove(name_File + f"/{z}")
    print(list_)


if os.path.exists(config_directory):
    print("yes")
else:
    os.mkdir(config_directory)
    os.mkdir(browser_directory)
    config_string_values()
    os.mkdir(music_directory)
    os.mkdir(programms_direcotry)
    with open(config_programms, 'w') as f:
        print("as")
    config_string_values()
    print("Creating directory config...")
    with open(config_browser, 'w') as f:
        print("as")

start_settings_code()
get_config_data()
print(config_directory)
def command():
    with sr.Microphone() as source:
        r = sr.Recognizer()
        print("Говорите")
        audio = r.listen(source)
    try:
        zadanie = r.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали: " + zadanie)
    except sr.UnknownValueError:
        print("error")
        zadanie = command()

    return zadanie

def makeSomething(zadanie):
    global is_track
    if 'стоп' in zadanie:
        comamnds_check = False
        talk("Да, конечно, без проблем")
        sys.exit()
    elif 'имя' in zadanie:
        comamnds_check = False
        text2 = f"Меня зовут {bot_name}. Я голосовой помощник."
        talk(text2)
    elif 'открой программу' in zadanie:
        zadanie2 = zadanie.replace("открой программу", "")
        zadanie2 = zadanie2[1:]
        file1 = open(config_programms, "r", encoding='utf-8')
        lines = file1.readlines()
        for line in lines:
            partss = line.split(";")
            print(partss)
            if zadanie2 in partss:
                print("fing programm")
                talk("Программа найдена, начинаю запуск...")
                program_paths = f"{partss[1]}"
                print(program_paths)
                os.system(program_paths)
        file1.close()   
        comamnds_check = False
    elif 'время' in zadanie:    
        comamnds_check = False
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        text = "Текущее время: " + current_time
        talk(text)
    elif 'включи песню' in zadanie:
        comamnds_check = False
        zadanie2 = zadanie.replace("включи песню", "")
        zadanie2 = zadanie2[1:]
        check_track = False
        print(zadanie2)
        list_music = os.listdir(music_directory)
        print(list_music)
        for z in list_music:
            print(z)
            if '.mp3' in z:
                print("find mp3 file")
                music_files = (f"{music_directory}/{z}")
                print(music_files)
                if zadanie2 in z:
                    if check_track == False:
                        print('find music')
                        music_play(music_files, f"Включаю песню, {zadanie2}")
                        check_track = True
                    else:
                        talk("Найденно два файла с одноименным названием. Ошибка")
                        check_track = False
        if check_track == False:
            talk("Не найденная песня")
    elif 'проверить целостность файлов' in zadanie:
        comamnds_check = False
        if os.path.exists(config_directory):
            if os.path.exists(programms_direcotry) == False:
                os.mkdir(programms_direcotry)
            elif os.path.exists(config_programms) == False:
                with open(config_programms, 'w') as f:
                    print("as")
            elif os.path.exists(music_directory) == False:
                os.mkdir(music_directory)
            elif os.path.exists(config_boss_file) == False:
                config_string_values()
            elif os.path.exists(browser_directory) == False:
                os.mkdir(browser_directory)
            elif os.path.exists(config_browser) == False:
                with open(config_browser, 'w') as f:
                    print("as")
    elif 'открой сайт' in zadanie:
        zadanie2 = zadanie.replace("открой сайт", "")
        zadanie2 = zadanie2[1:]
        file1 = open(config_browser, "r", encoding='utf-8')
        lines = file1.readlines()
        for line in lines:
            parts = line.split(";")
            print(parts)
            if zadanie2 in parts:
                print("find site")
                talk("Сайт найден, открываю....")
                url = f"{parts[1]}" 
                webbrowser.open(url, new=2)
        file1.close()
        comamnds_check = False
    elif 'выключи компьютер' in zadanie:
        comamnds_check = False
        talk("Выключаю")
        os.system("shutdown /s /t 1") 
    elif 'выключи музыку' in zadanie:
        global running
        if is_track is True:
            mixer.music.stop()
            is_track = False
            if running is True:
                main_func()
                running = False
            talk("Музыка успешна выключена.")
        else:
            talk("Сейчас ничего не играет")
        comamnds_check = False
    elif 'звук' in zadanie:
        if is_track is True:
            if playlist_check is False:
                zadanie2 = zadanie.replace("звук", "")
                zadanie2 = zadanie2[1:]
                numbers = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "ноль"]
                if zadanie2 in numbers:
                    numbersjson = {
                        "один": 1,
                        "два": 2,
                        "три": 3,
                        "четыре": 4,
                        "пять": 5,
                        "шесть": 6,
                        "семь": 7,
                        "восемь": 8,
                        "девять": 9,
                        "ноль": 0
                    }
                    zadanie2 = numbersjson.get(zadanie2)
                try:
                    volume = int(zadanie2)
                    volume  = volume / 100
                    pygame.mixer.music.set_volume(volume)
                    with open(config_boss_file, 'r') as file: 
                        data = file.readlines() 
                    data[4] = f"volumeSound={volume}\n"
                    with open(config_boss_file, 'w') as file: 
                        file.writelines(data)
                except:
                    print(volume)
                    talk("Неопознанное число громкости, попробуйте еще раз.")
            else:
                talk("Сейчас ничего не играет")

        comamnds_check = False
    elif 'убрать голос' in zadanie:
        comamnds_check = False
        talk("Голос убран")
        global bot_voice
        bot_voice = 0
            
        with open(config_boss_file, 'r') as file: 
            data = file.readlines() 
  
        print(data) 
        data[0] = "voiceAssistentSaying=0\n"
  
        with open(config_boss_file, 'w') as file: 
            file.writelines(data) 
    elif 'включить голос' in zadanie:
        comamnds_check = False
        bot_voice = 1
            
        with open(config_boss_file, 'r') as file: 
            data = file.readlines() 
  
        print(data) 
        data[0] = "voiceAssistentSaying=1\n"
  
        with open(config_boss_file, 'w') as file: 
            file.writelines(data)
        talk("голос включен")
    elif 'включи повтор песни' in zadanie:
        comamnds_check = False
        if is_track is True:
            time_music = pygame.mixer.music.get_pos() / 1000
            print(f"time: {time_music}\n")
            mixer.music.stop()
            mixer.music.load(last_load_music)
            mixer.music.play(-1, time_music)
            global volume_sound
            mixer.music.set_volume(volume_sound)
            with open(config_boss_file, 'r') as file: 
                data = file.readlines() 
            data[3] = "repeatMusic=-1\n"
            with open(config_boss_file, 'w') as file: 
                file.writelines(data)
    elif 'выключи повтор песни' in zadanie:
        comamnds_check = False
        if is_track is True:
            time_music = pygame.mixer.music.get_pos() / 1000
            print(f"time: {time_music}\n")
            mixer.music.stop()
            mixer.music.load(last_load_music)
            mixer.music.play(0, time_music)
            mixer.music.set_volume(volume_sound)
            with open(config_boss_file, 'r') as file: 
                data = file.readlines() 
            data[3] = "repeatMusic=0\n"
            with open(config_boss_file, 'w') as file: 
                file.writelines(data)
    elif 'включи плейлист' in zadanie:
        zadanie2 = zadanie.replace("включи плейлист", "")
        zadanie2 = zadanie2[1:]
        directory_playlist = "a"
        check_track = False
        print(zadanie2)
        list_music = os.listdir(music_directory)
        print(list_music)
        for z in list_music:
            print(z)
            name_playlist = "playlist." + zadanie2 
            if name_playlist in z:
                directory_playlist = music_directory + "/" + name_playlist
        playlist_directory_name_music = []
        if directory_playlist != "a":
            files = os.listdir(directory_playlist)
            if len(files) > 0:
                for x in files:
                    if ".mp3" in x:
                        print(f"find mp3 file: {x}")
                        music_playlist_directory = directory_playlist + "/" + x
                        playlist_directory_name_music.append(music_playlist_directory)
                print(f"playlist list: {playlist_directory_name_music}")
                playlist_play(playlist_directory_name_music)
                main_func()
def talk(text):
    if bot_voice == 1:
        t1 = gtts.gTTS(bot_appeal + ", " + text, lang='ru')
        t1_name = "last-mp3.mp3"
        t1.save(t1_name)
        playsound(t1_name)
        os.remove(t1_name)
    comamnds_check = True
def music_play(directory, text):
    global last_load_music
    global bot_repeat_music
    last_load_music = directory
    if bot_voice == 1:
        t1 = gtts.gTTS(bot_appeal + ", " + text, lang='ru')
        t1_name = "last-mp3.mp3"
        t1.save(t1_name)
        playsound(t1_name)
        os.remove(t1_name)
        time.sleep(2)
    global volume_sound
    mixer.music.load(directory)
    mixer.music.play(bot_repeat_music)
    print(f"volume: {volume_sound}")
    mixer.music.set_volume(volume_sound)
    comamnds_check = True
    global is_track
    is_track = True

def playlist_play(playlist):
    comamnds_check = True
    global playlist_check
    playlist_check = True
    pygame.mixer.music.load ( playlist.pop() )  
    pygame.mixer.music.queue ( playlist.pop() )
    global is_track
    global volume_sound
    global running
    is_track = True
    plylist_len = len(playlist)
    len_play = 0
    pygame.mixer.music.set_endevent(pygame.USEREVENT) 
    pygame.mixer.music.play()
    mixer.music.set_volume(volume_sound)
    running = True
    playlist_already_ready = 1
    while running:
        time.sleep(1)
        print("ads")
        if running is True:
            main_func()
            for event in pygame.event.get():
                len_play += 1
                print("track end")
                if len_play == plylist_len:
                    print("all tracks end")
                if event.type == pygame.USEREVENT:    # A track has ended
                    if len ( playlist ) > 0:       # If there are more tracks in the queue...
                        pygame.mixer.music.queue (playlist.pop())
                    else:
                        print(f"end: {playlist}")
                        pygame.mixer.music.queue ( playlist.pop() )
    print("end")

def main_func():
    while comamnds_check: 
        if keyboard.is_pressed('q'):
            print('true')
            print('You Pressed A Key!')
            makeSomething(command())
if playlist_already_ready == 0:
    main_func()
