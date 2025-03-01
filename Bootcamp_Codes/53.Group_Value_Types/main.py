def group_types(custom_list):
    int_keys = [item for item in custom_list if isinstance(item, int)]
    str_keys = [item for item in custom_list if isinstance(item, str)]

    # Create dictionaries using fromkeys()
    grouped_dict = dict.fromkeys(int_keys, "Integer")
    grouped_dict.update(dict.fromkeys(str_keys, "String"))

    return grouped_dict

# Example usage
custom_list = [10, "one", "two", "ten", 20, 30, "five", 40, "nine", 50]
print(group_types(custom_list))
