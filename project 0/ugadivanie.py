"Компьютер угадывает число меньше чем за 20 попыток"

import numpy as np


def random_predict(number: int = 1) -> int:
    count = 0
    min=1
    max=101
    while True:
        middle=round((min+max)/2)
        count += 1
        predict_number = np.random.randint(min, max)  
        if middle>predict_number:
            max=middle
        elif middle<predict_number:
            min=middle 
        else:
            print(f"Компьютер угадал загаданное число {predict_number} число за {count} попыток.")
            break
    return count
   
random_predict()
def score_game(random_predict) -> int:
    count_ls = []
    np.random.seed(1) 
    random_array = np.random.randint(1, 101, size=(1000)) 

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

score_game(random_predict)