import re
import os

# Get the user's selection for the output format they want.
output_option = input("\nType 1 to output your constants directly to your const_value_table.h header file. \nType 2 to output your constants to a new file which you can copy over to your const_value_table.h header file. This is handy if you want to see all of the constants you currently don't have in your header file. The output will be in \'new_constants_list.txt\'\n")
valid_option = False
# Keep asking for inputs until the user gives a valid input.
while valid_option != True:
	if output_option == "1" or output_option == "2":
		valid_option = True
		break
	else:
		output_option = input("\n\nInvalid option, try again \n\nType 1 to output your constants directly to your const_value_table.h header file. \nType 2 to output your constants to a new file which you can copy over to your const_value_table.h header file. This is handy if you want to see all of the constants you currently don't have in your header file. The output will be in \'new_constants_list.txt\'\n")
		
# Get the filename of the new constant value table.
new_table_filename = input("Enter the filename of the constant value table text file with your new constants (e.g. const_value_table700.txt): ")
new_table_filename_reformat = new_table_filename + '_rf.txt' # Make the file name for a new file for the reformatted lines from the new constant value table.
new_constants_list_filename = "new_constants_list.txt" # Filename to dump the list of constants not currently in the header file.

# Put all of the new constant value table entries into a list
print("Putting constant value table entries into list...")
with open(new_table_filename) as filehandle1:
	new_version_constants = filehandle1.readlines()
	for i in range(len(new_version_constants)):
		new_version_constants[i] = re.sub(r"(?i)^.+,", '', new_version_constants[i]) # Strip the hex values and comma from the beginning of each line to get only the constant names

# Write the reformatted lines to a new file
print("Reformatting constant value table...")
with open(new_table_filename_reformat, 'w+') as filehandle2:
	for listitem in new_version_constants:
		filehandle2.write('%s' % listitem)
		
# Strip any new lines from the end of each list entry of the reformated constant value lines, and place into new_version_constants_rf list
with open(new_table_filename_reformat) as filehandle2:
	new_version_constants_rf = filehandle2.readlines()
	for i in range(len(new_version_constants_rf)):
		new_version_constants_rf[i] = new_version_constants_rf[i].rstrip("\n")	

# Get the filename of the current constant value table header file
current_table_filename = input("Enter the filename of your constant value table header file (e.g. const_value_table.h): ")

lines_to_write = [] # Make a blank list for the lines for the new constants to write to const_value_table.h


# Compare the entries in the new constant value table text file to the one in the current constant value table header file

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

# Write new constants to file depending on option selected (lines formatted as necessary for use with the header file)
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

