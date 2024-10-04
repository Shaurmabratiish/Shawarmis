
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
import random
import keyboard
from datetime import datetime
mixer.init()
comamnds_check = True

name = "Великий шаурмабратииш пж бро кек лол анус"
bot_name = "залупа анусовая могила член"

is_track = False

config_directory = "" + os.path.dirname(__file__) + "/config"
config_boss_file = config_directory + "/фыв113.txt"
music_directory = config_directory + "/music"
programms_direcotry = config_directory + "/programms"
config_programms = programms_direcotry + "/config_programms.txt"
browser_directory = config_directory + "/browser"
config_browser = browser_directory + "/config_browser.txt"

def start_settings_code():
    name_File = os.path.dirname(__file__)
    list_ = os.listdir(name_File)
    print("start settings function")
    for z in list_:
        print(name_File + f"/{z}")
        if ".mp3" in z:
            os.remove(name_File + f"/{z}")
    print(list_)

start_settings_code()

if os.path.exists(config_directory):
    print("yes")
else:
    os.mkdir(config_directory)
    os.mkdir(browser_directory)

    os.mkdir(music_directory)
    os.mkdir(programms_direcotry)
    os.mkdir(config_programms)
    with open(config_programms, 'w') as f:
        print("as")
    with open(config_boss_file, 'w') as f:
        print("as")
    print("Creating directory config...")
    with open(config_browser, 'w') as f:
        print("as")
print(config_directory)
def command():
    with sr.Microphone() as source:
        r = sr.Recognizer()
        print("Говорите")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
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
    if is_track is False:
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
                parts = line.split(";")
                print(parts)
                if zadanie2 in parts:
                    print("fing programm")
                    talk("Программа найдена, начинаю запуск...")
                    program_path = f"{parts[1]}" 
                    subprocess.Popen(program_path)
            file1.close()   
            comamnds_check = False
            """
            try:
                program_path = "C:/Users/volnk/Downloads/Cristalix.exe" 
                subprocess.Popen(program_path)
                text = "Программа успешно запущена"
                talk(text) 
                print(f"Программа {program_path} успешно запущена.") 
            except FileNotFoundError: 
                print(f"Программа {program_path} не найдена.") 
            except Exception as e: 
                print(f"Произошла ошибка при запуске программы: {e}")
            """
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
                    with open(config_boss_file, 'w') as f:
                        print("as")
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
    if 'выключи музыку' in zadanie:
        if is_track is True:
            mixer.music.stop()
            is_track = False
            talk("Музыка успешна выключена.")
        else:
            talk("Сейчас ничего не играет")
        comamnds_check = False
    elif 'звук' in zadanie:
        if is_track is True:
            zadanie2 = zadanie.replace("звук", "")
            zadanie2 = zadanie2[1:]
            print(zadanie2)
            try:
                volume = int(zadanie2)
                volume  = volume / 100
                pygame.mixer.set_volume(volume)
            except:
                print(volume)
                talk("Неопознанное число громкости, попробуйте еще раз.")

            is_track = False
            talk("Музыка успешна выключена.")
        else:
            talk("Сейчас ничего не играет")
        comamnds_check = False 
def talk(text):
    t1 = gtts.gTTS(name + ", " + text, lang='ru')
    t1_name = "last-mp3.mp3"
    t1.save(t1_name)
    playsound(t1_name)
    comamnds_check = True
    os.remove(t1_name)
def music_play(directory, text):
    t1 = gtts.gTTS(name + ", " + text, lang='ru')
    t1_name = "last-mp3.mp3"
    t1.save(t1_name)
    playsound(t1_name)
    comamnds_check = True
    os.remove(t1_name)
    time.sleep(2)
    mixer.music.load(directory)
    global is_track
    is_track = True
    mixer.music.play()
while comamnds_check: 
    if keyboard.is_pressed('q'): 
        print('You Pressed A Key!')
        makeSomething(command())
