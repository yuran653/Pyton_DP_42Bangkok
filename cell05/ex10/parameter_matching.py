#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parameter_matching.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jgoldste <jgoldste@student.42bangkok.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/09 12:04:45 by jgoldste          #+#    #+#              #
#    Updated: 2024/02/09 12:04:45 by jgoldste         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

try:
	if (len(sys.argv) != 2):
		print("none")
	else:
		if (input("What was the parameter? ") == sys.argv[1]):
			print("Good job!")
		else:
			print("Nope, sorry...")
except:
	print("An error has been occurred", file=sys.stderr)
	sys.exit(1)