import pyautogui


class Event:

    def __init__(self, check_func, action_if_true, action_if_false):
        self.check_func      = check_func
        self.action_if_true  = action_if_true
        self.action_if_false = action_if_false

    def try_do_action(self, hand):
        if self.check_func(hand):
            if self.action_if_true:
                self.action_if_true(hand)
            return

        if self.action_if_false:
            self.action_if_false(hand)

events = []

def up_check(hand):
    return hand.joints[4].position.x > hand.joints[3].position.x

def up_true_action(hand):
    pyautogui.keyDown('up', _pause=False)

def up_false_action(hand):
    pyautogui.keyUp('up', _pause=False)

up_event = Event(up_check, up_true_action, up_false_action)
events.append(up_event)

def down_check(hand):
    return abs(hand.joints[12].position.x - hand.joints[8].position.x) > 40

def down_true_action(hand):
    pyautogui.keyDown('down', _pause=False)

def down_false_action(hand):
    pyautogui.keyUp('down', _pause=False)

down_event = Event(down_check, down_true_action, down_false_action)
events.append(down_event)
