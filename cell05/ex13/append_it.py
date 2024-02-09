#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    append_it.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jgoldste <jgoldste@student.42bangkok.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/09 12:41:31 by jgoldste          #+#    #+#              #
#    Updated: 2024/02/09 12:41:31 by jgoldste         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if (len(sys.argv) < 2):
	print("none")
else:
	none = True
	for i in range(1, len(sys.argv)):
		if(sys.argv[i].endswith("ism") == False):
			print(sys.argv[i] + "ism")
			none = False
	if none == True:
		print("none")