#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scope_that.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jgoldste <jgoldste@student.42bangkok.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/09 20:24:05 by jgoldste          #+#    #+#              #
#    Updated: 2024/02/09 20:24:05 by jgoldste         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Add:
	@staticmethod
	def add_one(param):
		param += 1

var_int = 42
print(var_int)
Add.add_one(var_int)
print(var_int)
