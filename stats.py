#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  stats.py
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
import json
import settings
from subprocess import check_output

def get_highscores():
	"""Return current highscores"""
	return get()["highscores"]


def make_new_stats_file():
	"""Generate new stats file"""
	stats_var = {"highscores":{}, "wins":0, "losses":0, "largest number reached":4}
	with open("2048-stats.json", "w+") as stats:
		json.dump(stats_var, stats, indent=1)


def new_highscore(score):
	"""Report New highscore"""
	try:
		with open("2048-stats.json", "r") as stats_file:
			stats = json.load(stats_file)
		for each in stats["highscores"]:
			if score < stats["highscores"][each]:
				continue
			else:
				username = check_output("whoami")
				request = input("New High Score: %s, Username (default: %s): " % (score, username))
				if request not in ("", " ", None):
					username = request
				stats["highscores"][username] = score
		if len(stats["highscores"]) >= settings.query("highscore log length"):
			stats["highscores"] = stats["highscores"][0:settings.query("highscore log length") + 1]
		with open("2048-stats.json", "w") as stats_file:
			json.dump(stats, stats_file, indent=1)
	except FileNotFoundError:
		make_new_stats_file()
		new_highscore(score)


def get_wins():
	"""return current wins"""
	return get()["wins"]


def get_losses():
	"""return current losses"""
	return get()["losses"]


def get_record():
	"""return current win:loss record"""
	stats = get()
	return "%s:%s" % (stats["wins"], stats["losses"])


def new_win():
	"""records new win"""
	stats = get()
	stats["wins"] = stats["wins"] + 1
	with open("2048-stats.json", "w") as stats_file:
		json.dump(stats, stats_file, indent=1)

		
def new_loss():
	"""records new loss"""
	stats = get()
	stats["losses"] = stats["losses"] + 1
	with open("2048-stats.json", "w") as stats_file:
		json.dump(stats, stats_file, indent=1)

def new_largest_number(number):
	"""Set new largest number. Checks if new number is actually larger, so this can be safely called blindly.

	Returns False if number is equal to or less than already recorded number. No changes are made to stats file in this instance
	Returns True and writes new stats to file if number is greater than recorded greatest number.
	"""
	stats = get()
	if stats["largest number reached"] >= number:
		return False
	else:
		stats["largest number reached"] = number
		with open("2048-stats.json", "w") as stats_file:
			json.dump(stats, stats_file, indent=1)
		return True

def get():
	"""get stats"""
	try:
		with open("2048-stats.json", "r") as stats:
			return json.load(stats)
	except FileNotFoundError:
		make_new_stats_file()
		return {"highscores":{}, "wins":0, "losses":0, "largest number reached":4}
