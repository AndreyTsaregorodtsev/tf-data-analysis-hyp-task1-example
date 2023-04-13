import pandas as pd
import numpy as np
from scipy.stats import norm

chat_id = 297386717 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    a1 = x_success/x_cnt
    a2 = y_success/y_cnt
    d = np.sqrt((a1 * (1 - a1) / x_cnt) + (a2 * (1-a2) / y_cnt))
    z = (a2-a1)/d
    dec = z > norm.ppf(1-0.09)
    return dec
