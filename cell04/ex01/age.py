#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    age.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jgoldste <jgoldste@student.42bangkok.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/08 17:05:30 by jgoldste          #+#    #+#              #
#    Updated: 2024/02/08 17:05:30 by jgoldste         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

impi
import sys

try:
	age = int(input("Please tell me your age: "))
	print(f"You are currently {age} years old.")
	for i in range(10, 31, 10):
		print(f"In {i} years, you'll be {age + i} years old.")
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