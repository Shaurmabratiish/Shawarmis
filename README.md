----------------------------
READ ME
--------------
Shawarmis - Помощник-Асисстент для продвинутой работы в сети "Интернет", либо же работы с ПК.

- Для исполнения команд, следует зажать клавишу "Q". И начать говорить вашу команду.

При запуске пайтон-файла, в вашей директории, где находился Python-File, создатся директория "config". В ней вы сможете найти "config_data.txt". Это основной конфиг бота. Так - же, помимо него, создается еще 3 директории. Каждая отвечает за свою сферу обслуживания.

 "Browser"
  - в этой директории один текстовый файл, в котором пусто. Но! Вы можете его настроить. Просто добавьте некторые параметры.
  - Допустим, напишем:
    - youtube;https://youtube.com/
  - "youtube" - это фраза/команда, при произношении "открой сайт {фраза команда}", открывается URL-ccылка сайта, которая идет после ";"
  - Таких команд можно добавлять сколько угодно.
    
 "music"
   - в этой директории пусто, но, так же как и с прошлой, можно добавлять фразы, которые будут включать определенный трек.
   - засуньте в эту папку, любой .mp3 файл, и назовите его "алые розы.mp3". При произношении команды "включи песню {алые розы]",
   - он найдет одноименный .mp3 файл и включит вам его.
   - **Вспомогательные Команды:**
       - "выключи музыку"
           - выключает текущую песню.
       - "звук {число от 1 до 100}"
           - устанавливает громоксть звука песни.
       - "Включить повтор песни"
           - включает повтор песни, можно изменить в конфиге
