import pandas as pd
import numpy as np


chat_id = 297386717 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    p1 = x_success/x_cnt
    p2 = y_success/y_cnt
    if(p1-p2>0.09):
      return True
    else:
      return False
