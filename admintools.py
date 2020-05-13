import collections
import copy
import numpy as np
import re


def check_action(message):
    """Check if user wishies to peform an action.

    Gets user input and then returns True or False based on input. If input is
    not valid, user is asked again until vaild input provided. Valid input is
    'y' or 'n'.
    
    Args:
        message (str): Message to be displayed to user.
        
    Returns:
        True if user wants to perform the action, False otherwise.
    """
    repeat = ''
    while repeat == '':
        repeat = input(message + ' y or n: ')
        if repeat.lower() not in ['y', 'n']:
            print('\nThat is not a valid answer! Please try again.')
            repeat = ''
        elif repeat.lower() == 'y':
            return True
        else:
            return False


def check_email(email):
    """Check if email address is in a valid format.

    Checks if the email message is greater than 2 characters, contains an '@'
    symbol with text before it, text after it, a period, and some more text.
    Note: email addresses with only two characters between @ and . will fail.

    Args:
        email (str): Email address to be validated.

    Returns:
        True if email is in a valid format, False otherwise.
    """
    if len(email) > 2:
        x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]\S+[.]\S+[a-zA-Z]', email)
        if len(x) > 0:
            return True
    return False


def check_email_2(email):
    """Check if email address is in a valid format.

    Checks if the email message is greater than 2 characters, contains an '@'
    symbol with text before it, text after it, a period, and some more text.
    Note it is not very accurate - only checks that there is an @ and a . in
    the email address.

    Args:
        email (str): Email address to be validated.

    Returns:
        True if email is in a valid format, False otherwise.
    """
    if len(email) > 2:
        x = re.findall('^.*?@.*?\..*?$', email)
        if len(x) > 0:
            return True
    return False


def check_is_float(value):
    """Check if value can be converted to a float.
    
    Tries to convert the value to a float. Used to make sure that a value
    is a number.
    
    Args:
        value (str): String to check.
    
    Returns:
        True if value is a number (can be converted to a float), False 
        otherwise.
    """
    try:
        float(value)
        return True
    except ValueError:
        return False


def check_is_int(value):
    """Check if value can be converted to an integer.
    
    Tries to convert the value to an integer. Used to make sure that a value
    is a number.
    
    Args:
        value (str): String to check.
    
    Returns:
        True if value is a number (can be converted to an int), False 
        otherwise.
    """
    try:
        int(value)
        return True
    except ValueError:
        return False


def check_lead_zero(to_check):
    """Check if a number has a leading 0.

    Args:
        to_check (str): The number to be checked.

    Returns:
        True if a leading 0 is found or the string is empty, False otherwise.
    """
    if str(to_check) in (None, ''):
        return True
    elif str(to_check[0]) != '0':
        return False
    else:
        return True


def check_repeat():
    """Check if repeating with another action.

    Gets user input and then returns True or False based on input. If input is
    not valid, user is asked again until vaild input provided. Valid input is
    'y' or 'n'.
    
    Returns:
        True if user wants to perform another action, False otherwise.
    """
    repeat = ''
    while repeat == '':
        repeat = input('\nDo you want to prepare another file? y/n --> ')
        if repeat.lower() not in ['y', 'n']:
            print('\nThat is not a valid answer! Please try again.')
            repeat = ''
        elif repeat.lower() == 'y':
            return True
        else:
            return False


def check_repeat_help():
    """Check if repeating with another help action.

    Gets user input and then returns True or False based on input. If input is
    not valid, user is asked again until vaild input provided. Valid input is
    'y' or 'n'.
    
    Returns:
        True if user wants to perform another help action, False otherwise.
    """
    repeat = ''
    while repeat == '':
        repeat = input('\nDo you want to view another help file entry? y/n '
                       '--> ')
        if repeat.lower() not in ['y', 'n']:
            print('\nThat is not a valid answer! Please try again.')
            repeat = ''
        elif repeat.lower() == 'y':
            return True
        else:
            return False


def confirm_files(f_name, r_files, sort=False):
    """Print required files and have user press enter to continue.
    
    Orders the list on alphabetical order prior to displaying.

    Args:
        f_name (str): Name of file that is being processed.
        r_files (list): List of files that need to be present.
        sort (bool): If True sorts returned list, else list returned in
        order it is received.
    """
    if sort:
        r_files.sort()
    if len(r_files) == 1:
        text_f = 'this file is'
    else:
        text_f = 'these files are'
    print('\nTo process the {} the following files are required:\n'.format
          (f_name))
    for file in r_files:
        print(file)
    print('\nPlease make sure that {} in the required folder and are updated '
          'correctly before proceeding.'.format(text_f))
    input('\nPress the enter key to continue processing the {} file '
          '--> '.format(f_name))


def convert_to_float(item):
    """Convert a string to a float.
    
    Checks if an item can be converted to a float and returns it as a float if
    it can. Returns False if it cannot be converted to float.
    
    Args:
        item (str): String to be converted to a float.
        
    Returns:
        item as a float.
    """
    if check_is_float(item):
        return float(item)
    else:
        return False


def convert_to_int(item):
    """Convert a string to an integer.
    
    Checks if an item can be converted to an int and returns it as an int if it
    can. Returns False if it cannot be converted to an int.
    
    Args:
        item (str): String to be converted to an integer.
        
    Returns:
        item as an integer.
    """
    if check_is_int(item):
        return int(item)
    else:
        return False


def convert_to_nan(item, values, matching=True):
    """Convert target strings to NaN.
    
    Converts target strings listed in values to NaN so they can be processed
    within a DataFrame, such as for removing specific rows. If matching=False,
    strings that do not those listed in values are converted to NaN. Note that
    it cannot take None as a value in values.
    
    Args:
        item (str): String to be checked. item is converted to a string if
        necessary.
        values (list): Values to be checked. If found, NaN is returned (if 
        matching=True) or item is returned. If matching=False, this is
        reversed.
        matching (bool): If True, matching values are returned as NaN and non-
        matching are returned as passed (item). If False, non-matching values
        are returned as NaN and matching values are returned as passed (item).
        
    Returns:
        item or NaN (str): Depending on status of matching and if found or not.
    """
    # Convert to NaN if item is found in values
    if matching:
        if str(item) in map(str, values):
            return np.nan
        else:
            return item
        # Convert item to NaN if not found in values
    else:
        if str(item) in map(str, values):
            return item
        else:
            return np.nan
            

def convert_to_tuples(raw_data):
    """Convert lists to tuples.

    Takes a list of lists and converts each list to a tuple so that it can be
    saved to a CSV file.

    Args:
        raw_data (list): Lists to be converted.

    Returns:
        processed_data (list): Data in tuples.
    """
    processed_data = []
    for item in raw_data:
        output_tuple = tuple(item)
        processed_data.append(output_tuple)
    return processed_data


def convert_to_value(item, target_values, value, matching=True):
    """Convert target strings to NaN.
    
    Converts target strings listed in target_values to value so they can be
    processed within a DataFrame, such as for removing specific rows. If
    matching=False, strings that do not those listed in values are converted to
    value. Note that it cannot take None as a value in values.
    
    Args:
        item (str): String to be checked. item is converted to a string if
        necessary.
        target_values (list): Values to be checked. If found, value is returned
        (if matching=True) or item is returned. If matching=False, this is
        reversed.
        value (str): Value that is to be returned if taget_values check is
        positive (respective to matching)
        matching (bool): If True, matching values are returned as value and 
        non-matching are returned as passed (item). If False, non-matching
        values are returned as NaN and matching values are returned as passed
        (item).
        
    Returns:
        item or value (str): Depending on status of matching and if found or
        not.
    """
    # Convert to value if item is found in taget_values
    if matching:
        if str(item) in map(str, target_values):
            return value
        else:
            return item
        # Convert item to value if not found in values
    else:
        if str(item) in map(str, target_values):
            return item
        else:
            return value


def copy_dict_reset(source_dict):
    """Copy a dictionary and reset values to 0.
    
    Args:
        source_dict (dict): Dictionary to be copied.
        
    Returns:
        new_dict (dict): New dictionary with values set to 0.
    """
    new_dict = {}
    for key in source_dict.keys():
        new_dict[key] = 0
    return new_dict


def create_dict(key_names):
    """Create a dictionary with provided keys and set values to 0.
    
    Args:
        key_names (list): Keys to be added to dictionary.
        
    Returns:
        created_dict (dict): Dictionary with key values set to 0.
    """
    created_dict = {}
    for item in key_names:
        created_dict[item] = 0
    return created_dict


def create_ordered_dict(items):
    """Creates an ordered dictionary from a list of items.
    
    Each item is added to a dictionary. The position of the item is set as the
    key value. These are set in the order that the items are supplied in the
    items list. The dictionary can then be returned in order by iterating over
    the dictionary keys and sorting on the key values.
    
    Args:
        items (list) List of items in the desired order.
        
    Returns:
        items_dict (dict): Ordered items in a dictionary.
    """
    items_dict = {}
    n = 0
    # Add each item to dictionary and set value to its position in list
    for item in items:
        items_dict[item] = n
        n += 1
    return items_dict


def create_ordered_list(data_dict, items):
    """Creates an ordered list from a dictionary.
    
    Each dictionary key + value is added to a list, as a nested list.
    The position of the nested item is determined by the position of the key
    value in the items list. The returned list is the dictionary ordered on the
    keys.
    
    Args:
        data_dict (dict): Dictonary to be converted to an ordered list.
        items (list) List of dictionary keys in the desired order.
        
    Returns:
        results (list): Dictionary keys and values in an ordered list.
    """
    results = []
    for item in items:
        if item in data_dict:
            this_item = []
            this_item.append(item) # Add key
            this_item.append(data_dict[item]) # Add value
            results.append(this_item)
    return results


def debug_dict(test_dict):
    """Print out contents of a dictionary.

    Args:
        test_dict (dict): Dictionary to be printed out.
    
    Dict test from https://stackoverflow.com/questions/25231989/how-to-check-if
    -a-variable-is-a-dictionary-in-python
    """
    if isinstance(test_dict, collections.abc.Mapping):
        for k, v in test_dict.items():
            print(k, v)
    else:
        print('Passed object is not a dictionary')


def debug_list(test_list):
    """Print out contents of a list.
    
    Prints out the number of current item and its contents. Loops through
    entire list.

    Args:
        test_list (list): List to be printed out.
        
    List test from https://stackoverflow.com/questions/1835018/how-to-check-if-
    an-object-is-a-list-or-tuple-but-not-string
    """
    if isinstance(test_list,
                  collections.Sequence) and not isinstance (test_list, str):
        i = 0
        for item in test_list:
            print('Item {}'.format(i))
            print(str(item))
            i += 1
    else:
        print('Passed object is not a list')


def debug_list_item(test_item):
    """Print out a single list item.

    Args:
        test_item (string): Item to be printed.
    """
    print(test_item)


def extract_list(source_data, item_pos):
    """Extract a single list from a list of lists.
    
    Checks that an int is passed for item_pos then uses this to return the
    desired list. If item_pos is not an int then False is returned. Must catch
    False responses when calling function.

    Args:
        source_data (list): List containing all lists.
        item_pos (int): Location of the list to be extracted.

    Returns:
        (list): A single list from the list of lists.
    """
    # Check item_pos is an int
    if check_is_int(item_pos):
        pos = int(item_pos)
        # Check item_pos is a valid location
        if pos < len(source_data):
            return source_data[pos]
        else:
            return False
    else:
        return False


def extract_lists(source_data):
    """Extract each item from a nested list into one list.
    
    Takes a list which holds one list with a number of items. Extracts
    each item so that it is one item in one list. Returns a list with
    multiple items, from a list of one list.

    Args:
        source_data (list): A list holding one list with multiple items.

    Returns:
        extracted_list (list): A list with the contents of the inner list
        extracted.

    File structure (source_data):
        List within a list [][]
    """
    extracted_list = []
    i = 0
    while i < len(source_data[0]):
        item = source_data[0][i]
        extracted_list.append(item)
        i += 1
    return extracted_list


def extract_lists_all(source_data):
    """Extract each item from a nested list into one list.
    
    Takes a list which holds multiple lists with a number of items. Extracts
    each item so that it is one item in one list. Returns a list with
    multiple items, from a list of lists.

    Args:
        source_data (list): A list holding multiple lists with one or multiple
        items.

    Returns:
        extracted_list (list): A list with the contents of the inner lists
        extracted.

    File structure (source_data):
        Lists within a list [][]
    """
    # Check there are 2 or more items in source_data
    if len(source_data) == 1:
        return source_data[0]
    extracted_list = []
    i = 0
    while i < len(source_data):
        j = 0
        while j < len(source_data[1]):
            item = source_data[i][j]
            extracted_list.append(item)
            j += 1
        i += 1
    return extracted_list


def extract_list_item(source_data, item_pos):
    """Extract specific items from a list of lists.
    
    Extracts the item in item_pos from each list within a list of lists and
    returns a list with just the extracted items.
    
    Args:
        source_data (list): A list of lists.
        
    Returns:
        extracted_items (list): List of the extracted items.
    """
    extracted_items = []
    for item in source_data:
        target_item = item[item_pos]
        extracted_items.append(target_item)
    return extracted_items


def find_items(source_data, items, item_pos):
    """Display all records that contain a specific value in a specific column.
    
    Takes a list of lists and for each nested list checks for a specific values
    in the column specified by item_pos. If an identified value is found, the
    record is added to the returned list.
    
    Args:
        source_data (list): List containing nested lists.
        items (list): A list of items to look for.
        itemp_pos (int): Position of the column to search for the items in.
    
    Returns:
        found_records (list) List of nested lists for the identified records.
    """
    found_records = []
    for record in source_data:
        if record[item_pos] in items:
            found_records.append(record)
    return found_records


def find_missing(source, target):
    """Return items in source list but not in target list.
    
    Find items that are in the source list but not in the target list. Source
    and target should each be a list with a number of items.
    
    Args:
        source (list): Students in the sd_df data.
        target (list): Students in the lsd_tags_s data. 
    
    Returns:
        missing (list): Students that are missing from target list.
    """
    missing = []
    for item in source:
        if item not in target:
            missing.append(item)
    return missing


def get_common(list_a, list_b):
    """Return list with items that appear in both lists.
    
    Checks if list_a and list_b are both lists. If one is not a list then
    returns False. Must catch False returns when calling the function. If both
    list_a and list_b are in fact lists, will find items that are common to
    both lists.
    
    Args:
        list_a (list): First list of items.
        list_b (list): Second list of items.
    
    Returns:
        common (list): Items appearing in both lists.
    
    List test from https://stackoverflow.com/questions/1835018/how-to-check-if-
    an-object-is-a-list-or-tuple-but-not-string
    """
    common = []
    if isinstance(list_a,
                  collections.Sequence) and not isinstance (list_a, str):
        if isinstance(list_b,
                  collections.Sequence) and not isinstance (list_b, str):
            for student in list_a:
                if student in list_b:
                    common.append(student)
        else:
            return False
    else:
        return False
    return common


def remove_column(report_data, column_pos):
    """Remove a column from a set of data that consists of a list of lists.
    
    Removes a column from a list of lists by iterating over each nested list.
    List must contain lists - will not work on a single lists of characters or
    other objects.

    Args:
        report_data (list): Report data.
        column_pos (int): Position of the column to be removed.

    Returns:
        processed_data (list): Report data with the column removed.
    """
    raw_data = copy.deepcopy(report_data)
    processed_data = []
    for row in raw_data:
        this_item = row
        del this_item[column_pos]
        processed_data.append(this_item)
    return processed_data


def remove_items(data, items, action='r'):
    """Removes identified items from a list and returns updated list.
    
    Only works on lists of items, not on nested lists. If action flag is set to
    'k' then the items in items are kept and all items not in items are
    removed.
    
    Args:
        data (list): List of items to be processed.
        items (list): List of items to be checked against.
        action (str): Action to take on items in items:
            - 'r' Items in items are removed if found.
            - 'k' Items not in items are removed if found.
    
    Returns:
        updated_data (list): Data after processing.
    """
    updated_data = copy.deepcopy(data)
    print('\nProcessing items')
    num_students = len(updated_data) # For calculating % complete
    n = 0
    for item in updated_data:
        # Display progress
        n += 1
        progress = round((n/num_students) * 100)
        print("\rProgress: {}{}".format(progress, '%'), end="", flush=True)
        if item in items:
            if action == 'r': # Remove item
                updated_data.remove(item)
            elif action == 'k': # Keep item
                continue
            else:
                continue
        else: # item not in items
            if action == 'r': # Keep item
                continue
            elif action == 'k': # Remove item
                updated_data.remove(item)
            else:
                continue      
    print('\rFinished processing items')
    return updated_data


def remove_duplicates_list(raw_list):
    """Return a list with just unique items.
    
    Only works with a list of items, not with nested lists.
    
    Args:
        raw_list (list): List with duplicate items.
        
    Returns:
        unique_list (list):: List with only one instance of each item.
    """
    my_set = set(raw_list)
    unique_list = list(my_set)
    return unique_list


def replace_string(text, to_find, replacement):
    """Search for items in strings and replace.

    Search for characters or sequences of charaters in a string and replace
    them i.e. replace all commas.

    Args:
        text (str): The string to be searched.
        to_find (str): The character or sequence of characters to replace.
        replacement (str): The string to replace the character(s) with.

    Returns:
        String with characters replaced.
    """
    return text.replace(to_find, replacement)


def seed_dict(source_data, data_dictionary, seed):
    """Seed a dictionary with source data.
    
    Goes through a list of items and adds items not currently in
    data_dictionary to the dictionary. Added items are seeded with the passed
    seed. Updated dictionary is returned.
    
    Args:
        soure_data (list): List of items to add to dictionary (if not present).
        data_dictionary (dict): Dictionary to be updated.
        seed (str or int): Seed value to be added to new dictionary items.
    
    Returns:
        data_dictionary (dict): Updated dictionary.
    """
    # Get unique items in source_data)
    unique = set(source_data)
    unique_items = list(unique)
    # Find missing values and add to dictionary
    for item in unique_items:
        if item not in data_dictionary.keys():
            data_dictionary[item] = seed
    return data_dictionary


def sort_dict_values(dict_to_sort, sort_order='descending'):
    """Sort a dic and return as a list of tuples.
    
    Args:
        dict_to_sort (dict): Dict to sort.
        sort_order (str): How the data should be sorted. Allowed options:
            descending, ascending.
            
    Returns:
        orderd_list (list): Dict keys and values in required sort order.
        
    Source:
        https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-
        by-value
    
    Notes:
        kv[0] is the key
        kv[1] is the value
        -kv returns in reverse order.
    """
    if sort_order == 'descending':
        sorted_by_value = sorted(dict_to_sort.items(), key=lambda kv: (-kv[1],
                                 kv[0]))
    elif sort_order == 'ascending':
        sorted_by_value = sorted(dict_to_sort.items(), key=lambda kv: (kv[1],
                                 kv[0]))
    return sorted_by_value
        
    

def update_dict(data_dict, update_list):
    """Update the counts in a dictionary.
    
    Updates the counts (values) of a dictionary based on an update list. 
    data_dict must be a dictionary where the value for each key is the count
    of the appearance of each key in a set of data. Function adds to the count
    of each key each time the key appears in the update_list. If a value in the
    update key is not found it is added to the data_dict and set to 1.
    
    Args:
        data_dict (dict): Dictionary to be updated.
        update_list (list): List of items to be counted and updated in
        data_dict.
    """
    for item in update_list:
        if item in data_dict:
            data_dict[item] += 1
        else: # Create key and set to 1
            data_dict[item] = 1
    return data_dict