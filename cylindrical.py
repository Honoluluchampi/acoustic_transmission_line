import numpy as np

class cylindrical_tube :
  def __init__(self, lendth, area, rho) :
    self.length = length
    self.area = area
    self.rho = rho

  def z_m(w) :
    return 1j * w * self.rho * self.length / self.area
  
  def z_c(w) :
    return -1j * self.rho * self.c * self.c / w / self.area / self.length

  def matrix() :
    return lambda w : np.array([[1 + z_m(w) / z_c(w), 2 * z_m(w) + z_m(w)]])