#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  settings.py
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

def query_all():
	try:
		with open("2048-settings.json", "r") as read_file:
			return json.load(read_file)
	except FileNotFoundError:
		generate_new()
		return {"max X":4, "max Y":4, "2v4":6, "goal":2048, "highscore log length":10}


def query(search):
	settings = query_all()
	return settings[search]


def generate_new():
	settings = {"max X":4, "max Y":4, "2v4":6, "goal":2048, "highscore log length":10}
	with open("2048-settings.json", "w+") as dump_file:
		json.dump(settings, dump_file, indent=1)
	
def update(key, value):
	settings = query_all()
	settings[key] = value
	with open("2048-settings.json", "w+") as dump_file:
		json.dump(settings, dump_file, indent=1)
