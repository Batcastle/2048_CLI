#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  interface.py
#  
#  Copyright 2020 Thomas Castleman <contact@draugeros.org>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from copy import deepcopy

class Board():
	def __init__(self, x, y):
		"""Initialize 2048 Game Board"""
		self.game_board = [ [ " " for each in range( x ) ] for each1 in range( y ) ]
		self.previous_board = deepcopy(self.game_board)
		self.undo_done = False


	def assign_value(self, value_array):
		"""Assign values to boxes"""
		if value_array[0] >= len(self.game_board):
			x = len(self.game_board) - 1
		else:
			x = value_array[0]
		if value_array[1] >= len(self.game_board[0]):
			y = len(self.game_board[0]) - 1
		else:
			y = value_array[1]
		self.game_board[x][y] = value_array[2]
		self.undo_done = False


	def print(self):
		"""Print the game board"""
		for each in self.game_board:
			print("", end="|")
			for each1 in each:
				print("\t%s\t" % (each1), end="|")
			print("")
			for each1 in each:
				print("----------------", end="")
			print("")
		self.undo_done = False


	def swipe_right(self):
		"""Left Swipe function, returns total of all added numbers for score tracking"""
		total = 0
		for each in range(len(self.game_board)):
			for each1 in range(len(self.game_board[each])):
				# Add numbers that match, moving from left to right down the board
				# move numbers into empty spaces to their left
				if (each1 + 1) < len(self.game_board[0]):
					if self.game_board[each][each1] == " ":
						continue
					elif self.game_board[each][each1] == self.game_board[each][each1 + 1]:
						self.game_board[each][each1] = " "
						self.game_board[each][each1 + 1] = self.game_board[each][each1 + 1] * 2
						total = total + self.game_board[each][each1 + 1] 
					elif self.game_board[each][each1 + 1] == " ":
						self.game_board[each][each1 + 1] = self.game_board[each][each1]
						self.game_board[each][each1] = " "
		self.undo_done = False
		return total


	def swipe_left(self):
		"""Right swipe function, returns total of all added numbers for score tracking"""
		total = 0
		for each in range(len(self.game_board)):
			for each1 in range(len(self.game_board[each]) - 1, -1, -1):
				# Add numbers that match, moving from right to left down the board
				# move numbers into empty spaces to their right
				if (each1 - 1) >= 0:
					if self.game_board[each][each1] == " ":
						continue
					elif self.game_board[each][each1] == self.game_board[each][each1 - 1]:
						self.game_board[each][each1] = " "
						self.game_board[each][each1 - 1] = self.game_board[each][each1 - 1] * 2
						total = total + self.game_board[each][each1 - 1] 
					elif self.game_board[each][each1 - 1] == " ":
						self.game_board[each][each1 - 1] = self.game_board[each][each1]
						self.game_board[each][each1] = " "
		self.undo_done = False
		return total
		

	def check_for_goal(self, goal):
		self.undo_done = False
		for each in self.game_board:
			if goal in each:
				print("You Win!")
				return True
		return False
		
	def swipe_up(self):
		"""Downward swipe function, returns total of all added numbers for score tracking"""
		total = 0
		for each in range(len(self.game_board[0])):
			for each1 in range(len(self.game_board) - 1, -1, -1):
				# Add numbers that match, moving from bottom to top across the board
				# move numbers into empty spaces under them
				# refrence cells as: self.game_board[each1][each]
				if (each1 - 1) >= 0:
					if self.game_board[each1][each] == " ":
						continue
					elif self.game_board[each1][each] == self.game_board[each1 - 1][each]:
						self.game_board[each1][each] = " "
						self.game_board[each1 - 1][each] = self.game_board[each1 - 1][each] * 2
						total = total + int(self.game_board[each1 - 1][each])
					elif self.game_board[each1 - 1][each] == " ":
						self.game_board[each1 - 1][each] = self.game_board[each1][each]
						self.game_board[each1][each] = " "
		self.undo_done = False
		return total

		
	def swipe_down(self):
		"""Upward swipe function, returns total of all added numbers for score tracking"""
		total = 0
		for each in range(len(self.game_board[0])):
			for each1 in range(len(self.game_board)):
				# Add numbers that match, moving from top to bottom across the board
				# move numbers into empty spaces over them
				# refrence cells as: self.game_board[each1][each]
				if (each1 + 1) < len(self.game_board):
					if self.game_board[each1][each] == " ":
						continue
					elif self.game_board[each1][each] == self.game_board[each1 + 1][each]:
						self.game_board[each1][each] = " "
						self.game_board[each1 + 1][each] = self.game_board[each1 + 1][each] * 2
						total = total + self.game_board[each1 + 1][each] 
					elif self.game_board[each1 + 1][each] == " ":
						self.game_board[each1 + 1][each] = self.game_board[each1][each]
						self.game_board[each1][each] = " "
		self.undo_done = False
		return total


	def get_largest(self):
		"""return largest number on the board"""
		largest = 0
		for each in self.game_board:
			for each1 in each:
				if each1 == " ":
					continue
				elif each1 > largest:
					largest = each1
		self.undo_done = False
		return largest


	def undo(self):
		"""Users get a single undo."""
		self.undo_done = True
		self.game_board = deepcopy(self.previous_board)


	def check_for_loss(self):
		"""check for a lost game

		Returns False is game IS NOT lost
		Returns True if game IS lost
		"""
		if self.undo_done is False:
			return False
		else:
			return self.game_board == self.previous

	def query(self, X, Y):
		"""get value at given coordinates"""
		return self.game_board[X][Y]
		
