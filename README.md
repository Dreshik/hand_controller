# Hand Controller
# Описание
Контроллер с помощью mediapipe анализирует жесты руки и имитирует нажатие клавиш используя pyautogui.

# Подготовка к запуску
Перед работой необходимо установить модули:
~~~~
pip install opencv-python
pip install mediapipe
pip install pyautogu
~~~~
или можно воспользоваться файлом requirements.txt
~~~~
pip install -r requirements.txt
~~~~

#Как добавить имитацию нажатия клавиши
В events.py list events[] хранит правила по которым нажимается/отпускается та или иная кнопка.
Класс Event содержит 3 поля:
1. check_func - функция проверки жеста, которая возвращает true\false
2. action_if_true - действите, которые выполняется если check_func вернула true
3. action_if_false - действите, которые выполняется если check_func вернула false

При создании экземпляра сласса Event в качестве action_if_true и/или action_if_false можно передать 0.

#Примеры
В events_examples лежат примеры. Чтобы ими воспользоваться, достаточно скопировать содержимое любого файла в events.py.
