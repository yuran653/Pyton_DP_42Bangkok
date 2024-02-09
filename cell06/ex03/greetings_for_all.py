#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    greetings_for_all.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jgoldste <jgoldste@student.42bangkok.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/09 17:39:11 by jgoldste          #+#    #+#              #
#    Updated: 2024/02/09 17:39:11 by jgoldste         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Greets:
	def greetings(self, name="noble stranger"):
		if type(name) is str:
			print(f"Hello, " + name + ".")
		else:
			print("Error! It was not a name.")

a = Greets()
greetings = a.greetings

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)

# class Greets:
# 	def greetings(self, name=None):
# 		if name is None:
# 			print("Hello, noble stranger.")
# 		elif name is not None and type(name) is str:
# 			print(f"Hello, " + name + ".")
# 		else:
# 			print("Error! It was not a name.")

# a = Greets()
# greetings = a.greetings

# greetings('Alexandra')
# greetings('Wil')
# greetings()
# greetings(42)
