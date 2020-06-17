#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  2048_cli.py
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
import stats
import settings
import randomizer
import interface
import json
from sys import argv, stderr
from copy import copy
from time import sleep
VERSION = "0.0.1-alpha1"
HELP = "2048_cli, Version %s\n\t-h,\t--help\t\tPrint this help dialog and exit\n\t--settings\t\tPrint current settings\n\t--stats\t\tPrint current stats" % (VERSION)

def print_stats():
	"""Print current stats"""
	stats_to_print = stats.get()
	print("HIGHSCORES")
	print("----------")
	for each in stats_to_print["highscores"]:
		print("\t%s: %s" % (each, stats_to_print["highscores"][each]))
	print("\nRECORD")
	print("------")
	print(stats.get_record())
	print("\nHIGHEST NUMBER REACHED")
	print("----------------------")
	print(stats.get()["largest number reached"])

def query_settings():
	"""Print Current settings"""
	setting = settings.query_all()
	print(json.dumps(setting, indent=1))

def main():
	"""Main game"""
	setting = settings.query_all()
	board = interface.Board(setting["max X"], setting["max Y"])
	initial_points = randomizer.random_init(setting["max X"], setting["max Y"], setting["2v4"])
	board.assign_value(initial_points[0])
	board.assign_value(initial_points[1])
	score = 0
	previous_score = 0
	goal_reached = False
	while True:
		print("\nScore: %s" % (score))
		board.print()
		move = input("Use W/A/S/D to move, U to undo(only one undo in a row may be used): ").lower()
		if move == "w":
			previous_score = copy(score)
			score = score + board.swipe_up()
		elif move == "a":
			previous_score = copy(score)
			score = score + board.swipe_left()
		elif move == "s":
			previous_score = copy(score)
			score = score + board.swipe_down()
		elif move == "d":
			previous_score = copy(score)
			score = score + board.swipe_right()
		elif move == "u":
			score = copy(previous_score)
			board.undo()
		elif move in ("quit", "exit", "stop", "bye", "q"):
			__eprint__("Exit command received. Exiting without saving stats . . .")
			exit(1)
		else:
			__eprint__("%s not recognized. Please try again." % (move))
		if ((board.check_for_goal(setting["goal"])) and (not goal_reached)):
			goal_reached = True
			move = input("Continue?[Y/n]: ").lower()
			if move == "n":
				stats.new_largest_number(board.get_largest())
				stats.new_win()
				hs = stats.get_highscores()
				if len(hs) > 0:
					for each in hs:
						if hs[each] < score:
							stats.new_highscore(score)
				else:
					stats.new_highscore(score)
				exit(0)
		elif board.check_for_loss():
			print("You Lose!")
		else:
			while True:
				location = randomizer.random_location(setting["max X"], setting["max Y"])
				if board.query(location[0] - 1, location[1] - 1) == " ":
					break
				sleep(0.2)
			val = randomizer.random_val(setting["2v4"])
			board.assign_value((location[0] - 1, location[1] - 1, val))
		

def __eprint__(args, *kwargs):
	"""Print to stderr easier"""
	print(args, file=stderr, *kwargs)

if __name__ == '__main__':
	try:
		if argv[1] in ("-h", "--help"):
			print(HELP)
			exit(0)
		elif argv[1] == "--settings":
			query_settings()
			exit(0)
		elif argv[1] == "--stats":
			print_stats()
			exit(0)
		else:
			__eprint__("Argument not recognized: %s" % (argv[1]))
			exit(1)
	except IndexError:
		main()
