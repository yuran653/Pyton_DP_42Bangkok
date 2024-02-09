#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    upcase_it.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jgoldste <jgoldste@student.42bangkok.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/08 21:55:51 by jgoldste          #+#    #+#              #
#    Updated: 2024/02/08 21:55:51 by jgoldste         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if (len(sys.argv) == 1):
	print("none")
elif (len(sys.argv) > 1):
	print(sys.argv[1].upper())
