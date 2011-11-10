#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import exit
from snack import *

running = True

screen = SnackScreen()

g = GridForm(screen, "Glit", 1, 2)

h = Grid(2, 9)
g.add(h, 0, 0)

h.setField(Label('Title'), 0, 0, (1, 0, 1, 1))
h.setField(Entry(16), 1, 0, (1, 0, 1, 1))

for i in [i+1 for i in range(8)]:
    h.setField(Checkbox(str(i), isOn=True), 0, i, (1, 0, 1, 0))
    h.setField(Entry(16), 1, i, (1, 0, 1, 0))

j = Grid(3, 1)
g.add(j, 0, 1)

def reset():
    print 'reset'

resetbutton = Button("Reset t")
resetbutton.setCallback(reset)
j.setField(resetbutton, 0, 0, (1, 1, 0, 0))

exitbutton = Button("Exit")
exitbutton.setCallback(exit)
j.setField(exitbutton, 2, 0, (3, 1, 0, 0))

g.run()

screen.popWindow()
screen.finish()
