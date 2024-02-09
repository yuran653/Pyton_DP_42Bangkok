#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    methods_everywhere.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jgoldste <jgoldste@student.42bangkok.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/09 19:52:35 by jgoldste          #+#    #+#              #
#    Updated: 2024/02/09 19:52:35 by jgoldste         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class MethodsEverywhere:
	@staticmethod
	def shrink(str):
		print(str[slice(8)])
	@staticmethod
	def enlarge(str):
		print(str.ljust(8, 'Z'))

import sys

if (len(sys.argv) > 2):
	for i in sys.argv[1:]:
		if len(i) > 8:
			MethodsEverywhere.shrink(i)
		elif len(i) < 8:
			MethodsEverywhere.enlarge(i)
		else:
			print(i)
else:
	print("none")