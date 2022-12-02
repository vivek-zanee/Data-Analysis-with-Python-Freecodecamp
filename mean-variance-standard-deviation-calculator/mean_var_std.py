import numpy as np

def calculate(data):
  if len(data) != 9:
    raise ValueError("List must contain nine numbers.")

  ls = np.array(data).reshape(3,3)
  

  cal_mean = [list(np.mean(ls, axis=0)), list(np.mean(ls, axis=1)), float(np.mean(ls))]
  cal_var = [list(np.var(ls, axis=0)), list(np.var(ls, axis=1)), float(np.var(ls))]
  cal_std = [list(np.std(ls, axis=0)), list(np.std(ls, axis=1)), float(np.std(ls))]
  cal_max = [list(np.max(ls, axis=0)), list(np.max(ls, axis=1)), float(np.max(ls))]
  cal_min = [list(np.min(ls, axis=0)), list(np.min(ls, axis=1)), float(np.min(ls))]
  cal_sum = [list(np.sum(ls, axis=0)), list(np.sum(ls, axis=1)), float(np.sum(ls))]
  
  return {
    
      'mean': cal_mean,
      'variance': cal_var,
      'standard deviation': cal_std,
      'max': cal_max,
      'min': cal_min,
      'sum': cal_sum
  }