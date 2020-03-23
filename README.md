# SSBU-const_value_table-Updater
Updates the const_value_table.h (https://github.com/ultimate-research/code-mod-framework/blob/master/framework/include/useful/const_value_table.h) file used in the code mod framework (https://github.com/ultimate-research/code-mod-framework) for SSBU code mods.

This will allow you to update your const_value_table.h file by supplying the filename of your const_value_tableXYZ.txt file, e.g. const_value_table700.txt and the filename of your const value table header file (e.g. const_value_table.h).

An example const_value_tableXYZ file is included (const_value_table700.txt).

 - USAGE -
Run const_value_table_update.py and follow the instructions in the script.

There are two options: 
1. Output the constants directly to your header file formatted as necessary
2. Output the formatted lines to new_constants_list.txt for you to copy over to your header file, which is useful to see which constants you're currently missing

Option 1 currently appends the list of new constants to the end of the header file after the #endif // CONST_VALUE_TABLE_H line, so if you use the first option you'll have to move that line back down to the end of the file for now. Will be fixed shortly.

Compatible with Python 2 and above.
