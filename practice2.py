def show_even_numbers(*args):
    even_numbers_lst = [] 
    for i in args:
        try:
            if i%2 == 0:
                even_numbers_lst.append(i)
        except TypeError:
                    continue 
    return even_numbers_lst

def rewrite_list(func):
    count = 1
    for i in func:
        print(f'{count} - {i}')
        count += 1
    
rewrite_list(show_even_numbers(3, 8, 'hello', 100, [14, 13, 12], 12))