#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scan_it.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jgoldste <jgoldste@student.42bangkok.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/08 22:56:11 by jgoldste          #+#    #+#              #
#    Updated: 2024/02/08 22:56:11 by jgoldste         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import re
import sys

if (len(sys.argv) == 3):
	result = len(re.findall(sys.argv[1], sys.argv[2]))
	if result == 0:
		print("none")
	else:
		print(result)
else:
	print("none")

# import sys

# if (len(sys.argv) == 3):
# 	result = sys.argv[2].count(sys.argv[1])
# 	if result == 0:
# 		print("none")
# 	else:
# 		print(result)
# else:
# 	print("none")

