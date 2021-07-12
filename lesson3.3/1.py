generated_list = [i if i % 2 == 0 else None for i in range(10)]

# for i in range(10):
#     if i % 2 == 0:
#         generated_list.append(i)
#     else:
#         generated_list.append(None)


# print(generated_list)



source = {
    "key_1": "value",
    "key_2": "value",
    "broken_key": "value",
    "key_4": "value",
}


result = {key: value for key, value in source.items() if key.startswith("key")}

print(result)


# for key, value in source.items():
#     print(key, value)

