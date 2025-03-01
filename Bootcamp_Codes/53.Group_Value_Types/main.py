def group_types(p_list):
    out_dict = dict.fromkeys(p_list)
    for key in out_dict:
        if isinstance(key,int):
            out_dict[key] = "Integer"
        else:
            out_dict[key] = "String"
    return out_dict

# Example usage
custom_list = [10, "one", "two", "ten", 20, 30, "five", 40, "nine", 50]
print(group_types(custom_list))
