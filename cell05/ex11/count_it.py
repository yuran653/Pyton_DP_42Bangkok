#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count_it.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jgoldste <jgoldste@student.42bangkok.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/09 12:14:12 by jgoldste          #+#    #+#              #
#    Updated: 2024/02/09 12:17:02 by jgoldste         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if (len(sys.argv) < 2):
	print("none")
else:
	print(f"parameters: {len(sys.argv) - 1}")
	for i in sys.argv[1:]:
		print(f"{i}: {len(i)}")
		
# import sys

# if (len(sys.argv) < 2):
# 	print("none")
# else:
# 	print(f"parameters: {len(sys.argv) - 1}")
# 	for i in range (1, len(sys.argv)):
# 		print(f"{sys.argv[i]}: {len(sys.argv[i])}")
