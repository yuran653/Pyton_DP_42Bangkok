#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    your_namebook.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jgoldste <jgoldste@student.42bangkok.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/09 22:36:30 by jgoldste          #+#    #+#              #
#    Updated: 2024/02/09 22:36:30 by jgoldste         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Names:
	@staticmethod
	def array_of_names(persons):
		capitalized_names = [key.capitalize() + " " + value.capitalize() for key, value in persons.items()]
		return capitalized_names

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

array_of_names = Names.array_of_names

print(array_of_names(persons))
