#! /usr/bin/env python

import pygame
import time

def trace(z,y,screen,wire,color):
	z = [500 , 500]
	y = z.copy()
	for x in wire:
		if x[0] == 'R':
			y[0] += int(x[1:]) / 10
		elif x[0] == 'L':
			y[0] -= int(x[1:]) / 10
		elif x[0] == 'U':
			y[1] -= int(x[1:]) / 10
		elif x[0] == 'D':
			y[1] += int(x[1:]) / 10
		pygame.draw.aaline(screen, color, tuple(z), tuple(y))
		z = y.copy()


f = open("input.txt","r")
liste = []

wire = f.readline().rstrip("\n").split(",")
wire2 = f.readline().rstrip("\n").split(",")

screen = pygame.display.set_mode((1000, 1000))
running = 1
z = [500 , 500]
y = z.copy()
color = (0,0,255)
color1 = (0,255,0)
while running:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		running = 0
	screen.fill((255, 255, 255))
	####
	trace(z,y,screen,wire,color)
	trace(z,y,screen,wire2,color1)
	pygame.display.flip()