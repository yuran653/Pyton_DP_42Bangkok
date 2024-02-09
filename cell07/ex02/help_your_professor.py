#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    help_your_professor.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jgoldste <jgoldste@student.42bangkok.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/10 00:31:10 by jgoldste          #+#    #+#              #
#    Updated: 2024/02/10 00:31:10 by jgoldste         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from statistics import mean 

class Average:
	@staticmethod
	def average(class_dict):
		avarage_value = mean(class_dict.values())
		return avarage_value

class_3B = {
"marine": 18,
"jean": 15,
"coline": 8,
"luc": 9
}

class_3C = {
"quentin": 17,
"julie": 15,
"marc": 8,
"stephanie": 13
}

average = Average.average

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")
