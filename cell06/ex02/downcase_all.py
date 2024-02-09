#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    downcase_all.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jgoldste <jgoldste@student.42bangkok.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/09 16:53:06 by jgoldste          #+#    #+#              #
#    Updated: 2024/02/09 16:53:06 by jgoldste         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class DowncaseIt():
	def downcase_it(self, str):
		return str.lower()

import sys

a = DowncaseIt()
if len(sys.argv) > 1:
	for i in sys.argv[1:]:
		print(a.downcase_it(i))
else:
	print("none")
