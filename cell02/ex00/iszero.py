#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    iszero.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jgoldste <jgoldste@student.42bangkok.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/05 17:31:54 by jgoldste          #+#    #+#              #
#    Updated: 2024/02/05 18:30:12 by jgoldste         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

try:
	num = int(input())
	if num == 0:
		print("This number is equal to zero.")
	else:
		print("This number is different from zero.")
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