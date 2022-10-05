import cv2
import mediapipe as mp
from events import events

class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Joint:

    def __init__(self):
        self.position      = Position(0, 0)
        self.position_prev = Position(0, 0)

    def update_position(self, new_joint_position):
        self.position_prev = self.position
        self.position      = Position(new_joint_position.x, new_joint_position.y)

class Hand:

    def __init__(self):
        self.joints = {}
        for id in range(21):
            self.joints[id] = Joint()

    def update_joints_position(self, new_joints_position):
        for id in range(21):
            new_joint_position = new_joints_position[id]
            self.joints[id].update_position(new_joint_position)

if __name__ == '__main__':
    hand = Hand()
    cap = cv2.VideoCapture(0) #Камера
    hands = mp.solutions.hands.Hands(max_num_hands=1) #Объект ИИ для определения ладони
    draw = mp.solutions.drawing_utils #Для рисования ладони

    while True:
        #Закрытие окна
        if cv2.waitKey(1) & 0xFF == 27:
            break

        success, image = cap.read() #Считываем изображение с камеры
        image = cv2.flip(image, -1) #Отражаем изображение для корекктной картинки
        imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #Конвертируем в rgb
        results = hands.process(imageRGB) #Работа mediapipe
        joints_position = {}
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    joints_position[id] = Position(cx, cy)

                hand.update_joints_position(joints_position)
                for event in events:
                    event.try_do_action(hand)
                draw.draw_landmarks(image, handLms, mp.solutions.hands.HAND_CONNECTIONS) #Рисуем ладонь

        cv2.imshow("Hand", image) #Отображаем картинку