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
