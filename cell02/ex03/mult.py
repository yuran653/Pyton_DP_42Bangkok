#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mult.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jgoldste <jgoldste@student.42bangkok.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/05 19:11:50 by jgoldste          #+#    #+#              #
#    Updated: 2024/02/05 19:11:50 by jgoldste         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

try:
	a = int(input("Enter the first number:\n"))
	b = int(input("Enter the second number:\n"))
	result = a * b
	if result > 0:
		print(f"{a} x {b} = {result}\nThe result is positive.")
	elif result < 0:
		print(f"{a} x {b} = {result}\nThe result is negative.")
	else:
		print(f"{a} x {b} = {result}\nThe result is positive and negative.")
except ValueError as e:
	print("Error: ", e, file=sys.stderr)
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
