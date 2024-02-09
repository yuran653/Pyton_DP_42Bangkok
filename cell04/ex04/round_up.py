#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    round_up.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jgoldste <jgoldste@student.42bangkok.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/08 17:51:54 by jgoldste          #+#    #+#              #
#    Updated: 2024/02/08 17:51:54 by jgoldste         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# from math import *
from math import ceil
import sys

try:
	print(ceil(float(input("Give me a number: "))))
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
