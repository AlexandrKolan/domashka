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
   
random_predict()