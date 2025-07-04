data_list = [42, 3.14, "hello world", True, None, [1, 2, 3]]

for item in data_list:
    if isinstance(item, str):
        upper_str = item.upper()

        last_three = upper_str[-3:]
        print(f"original: {item}")
        print(f"uppercase: {upper_str}")
        print(f"last 3 letter: {last_three}")