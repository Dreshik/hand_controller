def up_check(hand):
    return abs(hand.joints[12].position.x - hand.joints[8].position.x) > 40

def up_true_action(hand):
    pyautogui.keyDown('up', _pause=False)

def up_false_action(hand):
    pyautogui.keyUp('up', _pause=False)

up_event = Event(up_check, up_true_action, up_false_action)
events.append(up_event)

def down_check(hand):
    return abs(hand.joints[16].position.x - hand.joints[20].position.x) > 40

def down_true_action(hand):
    pyautogui.keyDown('down', _pause=False)

def down_false_action(hand):
    pyautogui.keyUp('down', _pause=False)

down_event = Event(down_check, down_true_action, down_false_action)
events.append(down_event)

def left_check(hand):
    return hand.joints[5].position.x - hand.joints[4].position.x > 40

def left_true_action(hand):
    pyautogui.keyDown('left', _pause=False)

def left_false_action(hand):
    pyautogui.keyUp('left', _pause=False)

left_event = Event(left_check, left_true_action, left_false_action)
events.append(left_event)

def right_check(hand):
    print(hand.joints[5].position.x - hand.joints[4].position.x)
    return hand.joints[5].position.x - hand.joints[4].position.x < 0

def right_true_action(hand):
    pyautogui.keyDown('right', _pause=False)

def right_false_action(hand):
    pyautogui.keyUp('right', _pause=False)

right_event = Event(right_check, right_true_action, right_false_action)
events.append(right_event)
