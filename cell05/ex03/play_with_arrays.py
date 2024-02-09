#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    play_with_arrays.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jgoldste <jgoldste@student.42bangkok.co    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/02/08 21:16:53 by jgoldste          #+#    #+#              #
#    Updated: 2024/02/08 21:16:53 by jgoldste         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

original_array = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = []
for i in range(len(original_array)):
	if original_array[i] > 5:
		new_array.insert(len(new_array), original_array[i] + 2)
print(set(new_array))
