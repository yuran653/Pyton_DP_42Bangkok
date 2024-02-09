#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aff_rev_params.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jgoldste <jgoldste@student.42bangkok.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/08 22:09:18 by jgoldste          #+#    #+#              #
#    Updated: 2024/02/08 22:09:18 by jgoldste         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if (len(sys.argv) < 4):
	print("none")
else:
	print(list(reversed(sys.argv[1:])))

# import sys

# if (len(sys.argv) < 4):
# 	print("none")
# else:
# 	for i in range(len(sys.argv) - 1, 0, -1):
# 		print(sys.argv[i])
