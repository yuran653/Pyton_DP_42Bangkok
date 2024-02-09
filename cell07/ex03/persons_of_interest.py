#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    persons_of_interest.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jgoldste <jgoldste@student.42bangkok.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/09 21:45:52 by jgoldste          #+#    #+#              #
#    Updated: 2024/02/09 21:45:52 by jgoldste         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Dictionary:
	@staticmethod
	def famous_births(self,persons):
		sorted_persons = sorted(persons.items(), key=lambda x: x[1]["date_of_birth"])
		for person, details in sorted_persons:
			print(f"{details['name']} is a great scientist born in {details['date_of_birth']}.")

women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births = Dictionary.famous_births

famous_births(women_scientists)

