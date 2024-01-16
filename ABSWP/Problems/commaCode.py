
def format_list(list):
    if not list:
        return 'No items in the list'
    elif len(list) == 1:
        return list[0]
    else:
        formatted_string = ', '.join(list[:-1]) + ', and ' + list[-1]
        return formatted_string


spam = ['apples', 'bananas', 'tofu', 'cats']

print(format_list(spam))