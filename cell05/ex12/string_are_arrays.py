#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    string_are_arrays.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jgoldste <jgoldste@student.42bangkok.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/09 12:24:44 by jgoldste          #+#    #+#              #
#    Updated: 2024/02/09 12:24:44 by jgoldste         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if (len(sys.argv) != 2):
	print("none")
else:
	for i in range(0, len(sys.argv[1])):
		if sys.argv[1][i] == 'z':
			print(sys.argv[1][i], end='')
	print()
