massive = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3']

def calculate_sum_of_elements_in_array(array:list):
    for idx, elm in enumerate(array):
        try:
            sum_for_elm = 0
            for el in elm.split(','):
                sum_for_elm += int(el)
            print(f'Сума чисел для елемента №{idx+1} = {sum_for_elm}')
        except ValueError:
            print('Не можу це зробити!')

calculate_sum_of_elements_in_array(massive)