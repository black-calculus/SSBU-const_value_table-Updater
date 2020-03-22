import re
import os

output_option = input("\nType 1 to output your constants directly to your const_value_table.h header file. \nType 2 to output your constants to a new file which you can copy over to your const_value_table.h header file. This is handy if you want to see all of the constants you currently don't have in your header file. The output will be in \'new_constants_list.txt\'\n")
valid_option = False
while valid_option != True:
	if output_option == "1" or output_option == "2":
		valid_option = True
		break
	else:
		output_option = input("\n\nInvalid option, try again \n\nType 1 to output your constants directly to your const_value_table.h header file. \nType 2 to output your constants to a new file which you can copy over to your const_value_table.h header file. This is handy if you want to see all of the constants you currently don't have in your header file. The output will be in \'new_constants_list.txt\'\n")

new_table_filename = 'const_value_table700.txt'
new_table_filename = input("Enter the filename of your constant value table (e.g. const_value_table700.txt): ")
#new_table_filename_reformat = 'const_value_table_rf.txt'
new_table_filename_reformat = new_table_filename + '_rf.txt'
new_constants_list_filename = "new_constants_list.txt"

print("Putting constant value table entries into list...")
with open(new_table_filename) as filehandle1:
	new_version_constants = filehandle1.readlines()
	for i in range(len(new_version_constants)):
		new_version_constants[i] = re.sub(r"(?i)^.+,", '', new_version_constants[i])

print("Reformatting constant value table...")
with open(new_table_filename_reformat, 'w+') as filehandle2:
	for listitem in new_version_constants:
		filehandle2.write('%s' % listitem)
		
with open(new_table_filename_reformat) as filehandle2:
	new_version_constants_rf = filehandle2.readlines()
	for i in range(len(new_version_constants_rf)):
		new_version_constants_rf[i] = new_version_constants_rf[i].rstrip("\n")	

#line = "Hello World"
#line2 = "0x60fefa703bdc5050,LUA_SCRIPT_LINE_MAX"
#print(line2)
#line2 = re.sub(r"(?i)^.+,", '', line2)
#print(line2)

current_table_filename = input("Enter the filename of your constant value table header file (e.g. const_value_table.h): ")

lines_to_write = [] # Make a blank list for the lines for the new constants to write to const_value_table.h

print("Comparing constant value table entries against const_value_table.h...")	
with open(current_table_filename, 'r') as fh:
	for line in fh:
		current_table_constants = fh.readlines() # Read all the current lines from the current const_value_table.h into a list
		for i in range(len(current_table_constants)):
			# Grab only the constants from each line in const_value_table.h and place them into current_table_constants
			current_table_constants[i] = re.sub(r"(?i)^#define[ ]", '', current_table_constants[i]) # Remove first part of line before constant name
			current_table_constants[i] = re.sub(r"(?i)[ ].+", '', current_table_constants[i]) # Remove second part of line after constant name
			current_table_constants[i] = current_table_constants[i].rstrip("\n")

# Compare those lines with the entries in new_version_constants_rf
for i in range(len(new_version_constants_rf)):
	if new_version_constants_rf[i] in current_table_constants:
		print("Found constant. Skipping...")
		#break
	else:
		print("Appending new constant to list to write.")
		new_const_string = "#define " + new_version_constants_rf[i] + " lua_const(\"" + new_version_constants_rf[i] + '\")'
		lines_to_write.append(new_const_string) # Append new constant to the list of constants to write to the file.
		#break

print("Writing new constants to files...")
if output_option == "1":
	# Write all new constants to const_value_table.h
	with open(current_table_filename, 'a') as fh:
		for j in range(len(lines_to_write)):
			fh.write(lines_to_write[j] + "\n") # Write all the new constants to the file
		
if output_option == "2":
	# Write all new constants to new_constants_list.txt
	with open(new_constants_list_filename, 'a+') as fh:
		for j in range(len(lines_to_write)):
			fh.write(lines_to_write[j] + "\n") # Write all the new constants to the file

# Remove new_table_filename_rf.txt after we're done
os.remove(new_table_filename_reformat)

print("\n\nFinished!")


# String check testing, ignore this
#if new_version_constants_rf[0] not in current_table_constants:
#	print("Nope")
#else:
#	print("It's in there boss")

