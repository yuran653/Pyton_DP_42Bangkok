#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    to25.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jgoldste <jgoldste@student.42bangkok.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/06 10:26:12 by jgoldste          #+#    #+#              #
#    Updated: 2024/02/06 10:26:13 by jgoldste         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

try:
	num = int(input("Enter a number less than 25\n"))
	if num > 25:
		print("Error")
		sys.exit(1)
	while (num < 26):
		print(f"Inside the loop, my variable is {num}")
		num += 1
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

