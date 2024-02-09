#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    family_affairs.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jgoldste <jgoldste@student.42bangkok.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/09 23:32:45 by jgoldste          #+#    #+#              #
#    Updated: 2024/02/09 23:32:45 by jgoldste         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class FamilyAffairs:
	@staticmethod
	def find_the_redheads(family):
		red_head_members = filter(lambda item: item[1] == "red", family.items())
		return [member[0] for member in red_head_members]

dupont_family = {
"florian": "blond",
"marie": "red",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

find_the_redheads = FamilyAffairs.find_the_redheads

print(find_the_redheads(dupont_family))
