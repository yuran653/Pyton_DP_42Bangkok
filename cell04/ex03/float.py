#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    float.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jgoldste <jgoldste@student.42bangkok.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/08 17:34:16 by jgoldste          #+#    #+#              #
#    Updated: 2024/02/08 17:34:16 by jgoldste         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

try:
	num = float(input("Give me a number: "))
	if num == int(num):
		print("This number is an integer.")
	else:
		print("This number is a decimal.")
except ValueError as e:
	print("Error:", e, file=sys.stderr)
	sys.exit(1)
except EOFError:
	print("CTRL+D for what?", file=sys.stderr)
	sys.exit(1)
except KeyboardInterrupt:
	print("\nCTRL+C: exit OK", file=sys.stderr)
	sys.exit(0)
except:
	print("Undefined error", file=sys.stderr)
	sys.exit(1)
