def go_Left():
    if direction == 'left':
        print('Go left')

def go_Right():
    if direction == 'right':
        print('Go right')

def go_Up():
    if direction == 'up':
        print('Go up!')

def go_Down():
    if direction == 'down':
        print('Go down.')

direction = input('Choose a direction: up, down, left, right')
def chosen_direction():
    if direction == 'left':
        go_Left()
    elif direction == 'right':
        go_Right()
    elif direction == 'up':
        go_Up()
    elif direction =='down':
        go_Down()
    else:
        print('This is nog a legitime direction')

chosen_direction()