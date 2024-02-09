#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    free_range.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jgoldste <jgoldste@student.42bangkok.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/09 13:01:50 by jgoldste          #+#    #+#              #
#    Updated: 2024/02/09 13:01:50 by jgoldste         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if (len(sys.argv) == 3):
	if sys.argv[1].isdigit() == False or sys.argv[2].isdigit() == False:
		print("Argument(s) is/are not a number(s)")
	elif int(sys.argv[1]) >= int(sys.argv[2]):
		print("The first argument should be less than the second one")
	else:
		print(list(range(int(sys.argv[1]), int(sys.argv[2]) + 1)))
else:
	print("none")
