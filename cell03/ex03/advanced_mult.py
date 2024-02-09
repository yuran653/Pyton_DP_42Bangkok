#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    advanced_mult.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jgoldste <jgoldste@student.42bangkok.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/07 13:42:54 by jgoldste          #+#    #+#              #
#    Updated: 2024/02/07 13:42:54 by jgoldste         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) > 1:
	print("none")
	sys.exit(0)
i = 0
while i <= 10:
	print(f"Table de {i}: 0", end='')
	j = 0
	num = i
	while j < 10:
		print(f" {num}", end='')
		num += i
		j += 1
	print()
	i += 1
