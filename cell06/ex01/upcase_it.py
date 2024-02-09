#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    upcase_it.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jgoldste <jgoldste@student.42bangkok.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/09 16:43:46 by jgoldste          #+#    #+#              #
#    Updated: 2024/02/09 16:43:46 by jgoldste         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class UpcaseIt:
	def upcase_it(self, str):
		return str.upper()

a = UpcaseIt()
upcase_it = a.upcase_it()

print(upcase_it("hello"))

# def upcase_it(str):
# 	return str.upper()

# print(upcase_it("hello"))
