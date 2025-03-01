def value_lenght(p_dict):
    out_dict={}
    for key,value in p_dict.items():
        out_dict[key] = {value: len(value)} 
    return out_dict

names_dict = {1: "Elshad",
    2: "Renad",
    3: "Johanna",
    4:"Appmillers"
}


out_dict = value_lenght(names_dict)

# for key in out_dict:
#     for key1,value in out_dict[key].items():
#         print(key, key1 , value)

# for key in out_dict:
#     print(key, out_dict[key])

print (out_dict)

