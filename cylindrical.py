import numpy as np
import math

class cylindrical_tube :
  def __init__(self, length, area, rho, c) :
    self.length = length
    self.area = area
    self.rho = rho
    self.c = c

  def z_m(self, w) :
    return 1j * w * self.rho * self.length / self.area

  def z_c(self, w) :
    return -1j * self.rho * self.c * self.c / w / self.area / self.length

  def matrix(self) :
    return lambda w: np.array([
      [1 + self.z_m(w) / self.z_c(w), 2 * self.z_m(w) + self.z_m(w) * self.z_m(w) / self.z_c(w)],
      [1 / self.z_c(w),          1 + self.z_m(w) / self.z_c(w)]
    ])

def main() :
  N = 150  # number of segments
  L = 0.6  # total length
  a = 0.05  # radius of tube
  c = 340  # speed of sound
  rho = 1.21 # density

  x = [ i * L / N for i in range(N) ] # x coord in the tube
  freq_start = 1
  freq_end = 300
  df = 0.1
  freq = np.array([ freq_start + df * i for i in range(int((freq_end - freq_start) / df))])
  w = 2 * math.pi * freq # angular velocity
  k = w / c # wave number
  Z_rad = 0 # radiation impedance

  # calc input impedance for all frequency
  # for i in range (len(freq)) :


if __name__ == "__main__" :
    main()