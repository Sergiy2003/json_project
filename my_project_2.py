import json
         
def main():
    '''
    function helps to check content of json files
    >>>     Hello user
    Here is all keys
    dict_keys(['users', 'next_cursor', 'next_cursor_str', 'previous_cursor', 'previous_cursor_str', 'total_count'])
    Enter 1 to continue, 2 start again from the start -> 1
    Enter a key, value of what you want to know -> next_cursor
    1690854756298186010
    '''
    path = 'D:\\friends_list_AdamMGrant.json'
    with open(path, 'r', encoding='utf-8') as foul:
        text = json.load(foul)
    if type(text) == list:
        text == text[0]
    pre_text = text
    print('\tHello user')
    while True:
        if type(text) == dict:
            print('Here is all keys')
            print(text.keys())
        elif type(text) == list:
            print('type of a valuable is list')
            choice_type_1 = input('If you want to see all the inforamtion about elements in list enter 1, to miss enter anything  -> ')
            if choice_type_1 == '1':
                print(text)
        else: print(text)
        choice = input('Enter 1 to continue, 2 start again from the start -> ')
        if str(choice) == '2':
            text = pre_text
        if str(choice) == '1':
            key_choice = input('Enter a key, value of what you want to know -> ')
            text = text.get(key_choice)
main()