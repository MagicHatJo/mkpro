
import datetime

import config

def print_header(f, file_name):
    curr = datetime.datetime.now()
    file_len = len(file_name)
    name_len = len(config.HEADER_NAME)
    email_len = len(config.HEADER_EMAIL)
    f.write("# **************************************************************************** #\n")
    f.write("#                                                                              #\n")
    f.write("#                                                         :::      ::::::::    #\n")
    f.write("#    " + file_name + ((51 - file_len) * " ") + ":+:      :+:    :+:    #\n")
    f.write("#                                                     +:+ +:+         +:+      #\n")
    f.write("#    By: "+ config.HEADER_NAME + " <" + config.HEADER_EMAIL + ">" + ((40 - name_len - email_len) * " ") + "+#+  +:+       +#+         #\n")
    f.write("#                                                 +#+#+#+#+#+   +#+            #\n")
    f.write("#    Created: " + str(curr.year) + "/" + str('{:02}'.format(curr.month)) + "/" + str('{:02}'.format(curr.day)) + " ")
    f.write(str('{:02}'.format(curr.hour)) + ":" + str('{:02}'.format(curr.minute)) + ":" + str('{:02}'.format(curr.second)) + " ")
    f.write(config.HEADER_NAME + ((21 - name_len) * " ") + "#+#    #+#              #\n")
    f.write("#    Updated: " + str(curr.year) + "/" + str('{:02}'.format(curr.month)) + "/" + str('{:02}'.format(curr.day)) + " ")
    f.write(str('{:02}'.format(curr.hour)) + ":" + str('{:02}'.format(curr.minute)) + ":" + str('{:02}'.format(curr.second)) + " ")
    f.write(config.HEADER_NAME + ((20 - name_len) * " ") + "###   ########.fr        #\n")
    f.write("#                                                                              #\n")
    f.write("# **************************************************************************** #\n")
    f.write("\n")