#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  randomizer.py
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
import random
from time import sleep

def random_val(prob):
	"""Return either 2 or 4, depending on a certain probability"""
	seed = random.randint(0, 10)
	if seed < prob:
		return 2
	else:
		return 4


def random_location(max_x, max_y):
	"""Return random location on coordinate grid"""
	return (random.randint(0, max_x), random.randint(0, max_y))


def random_init(max_x, max_y, prob):
	"""Return two random dissimilar coordinates, with values of either 2 or 4"""
	location = random_location(max_x, max_y)
	element_one = [location[0], location[1], random_val(prob)]
	sleep(0.25)
	location = random_location(max_x, max_y)
	element_two = (location[0], location[1], random_val(prob))
	if element_two[0] == element_one[0]:
		if element_one[0] == max_x:
			element_one[0] = element_one[0] - 1
		else:
			element_one[0] = element_one[0] + 1
	return (element_one, element_two)


