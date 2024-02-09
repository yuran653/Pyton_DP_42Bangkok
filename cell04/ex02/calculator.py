#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    calculator.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jgoldste <jgoldste@student.42bangkok.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/08 17:28:45 by jgoldste          #+#    #+#              #
#    Updated: 2024/02/08 17:28:45 by jgoldste         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

try:
	a = int(input("Give me the first number: "))
	b = int(input("Give me the second number: "))
	print("Thank you!")
	print(f"{a} + {b} = {a + b}")
	print(f"{a} - {b} = {a - b}")
	if (b != 0):
		print(f"{a} / {b} = {a / b}")
	else:
		print("Division by zero is not allowed")
	print(f"{a} * {b} = {a * b}")
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
