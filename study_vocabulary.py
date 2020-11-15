import os
import sys
import time
import random
import tkinter as tk
from tkinter import messagebox

vocab_link = "vocabularies.txt"
DELAY_INTERVAL = 15   # seconds
SHOW_INTERVAL_FRENCH = 3
SHOW_INTERVAL_ENGLISH = 3


def read_file(link):
    french_vocabs = []
    english_vocabs = []
    with open(link) as f:
        for i, line in enumerate(f):
            french_vocab = line.split(" - ")[0]
            english_vocab = line.split(" - ")[1].strip()
            french_vocabs.append(french_vocab)
            english_vocabs.append(english_vocab)
    return french_vocabs, english_vocabs


def show_vocabulary(vocab, show_interval, background_color='white'):
    try:
        root = tk.Tk()
        # root.attributes("-fullscreen", True)

        # position for the window
        width = 100
        height = 50

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # calculate position x and y coordinates
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        # y = 0

        root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        root.configure(background=background_color)
        # put the frame on top of other
        root.call('wm', 'attributes', '.', '-topmost', True)

        # add text
        label = tk.Label(root, text=vocab, font=("Verdana", 15), background='white', foreground='black')
        # label = tk.Label(root, text=vocab, font=("Verdana", 15))
        label.pack()

        root.after(int(show_interval * 1000), root.destroy)
        root.mainloop()
        return
    except():
        print("tkinter does not work")


def main():
    original_time = time.time()
    french_vocabs, english_vocabs = read_file(vocab_link)

    while True:
        index = random.randint(0, len(french_vocabs) - 1)
        french_vocab = french_vocabs[index]
        english_vocab = english_vocabs[index]

        # show french_vocab, then english_vocab
        order = random.randint(0, 1)
        if order == 0:
            show_vocabulary(french_vocab, SHOW_INTERVAL_FRENCH, background_color='white')
            show_vocabulary(english_vocab, SHOW_INTERVAL_ENGLISH, background_color='gray')
        else:
            show_vocabulary(english_vocab, SHOW_INTERVAL_ENGLISH, background_color='gray')
            show_vocabulary(french_vocab, SHOW_INTERVAL_FRENCH, background_color='white')

        # show after each DELAY_INTERVAL seconds
        time.sleep(DELAY_INTERVAL)

        # read time every 5 minutes
        if (time.time() - original_time) / 1000 > 300:
            french_vocabs, english_vocabs = read_file(vocab_link)


if __name__ == '__main__':
    main()
