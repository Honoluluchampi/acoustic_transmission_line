import numpy as np
import math
import matplotlib.pyplot as plt

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
  l = L / N
  a = 0.05  # radius of tube
  A = math.pi * a * a # cross sectional area
  c = 340  # speed of sound
  rho = 1.21 # density
  Z_c = rho * c / A # characteristic impedance

  x = [ i * L / N for i in range(N) ] # x coord in the tube
  freq_start = 1
  freq_end = 3000
  df = 0.1
  freq = np.array([ freq_start + df * i for i in range(int((freq_end - freq_start) / df))])
  w = 2 * math.pi * freq # angular velocity
  k = w / c # wave number
  Z_rad = 0 # radiation impedance

  Z_in = []

  # calc input impedance for all frequency
  for i in range (len(freq)) :
    T = np.matrix([[1, 0], [0, 1]])
    for j in range (N-1, 0, -1) :
      m_acs = 0.5 * rho * l / A # acoustic mass of slice
      c_acs = A * l / (rho * c * c) # acoustic compliance
      Zi = 1j * w[i] * m_acs # inertance term
      Zc = -1j / (w[i] * c_acs) # compliance term

      T_tube = np.matrix([[1 + Zi / Zc, 2 * Zi + Zi * Zi / Zc], [1 / Zc, 1 + Zi / Zc]])
      # kl = k[i] * l
      # T_tube = np.matrix([[math.cos(kl), 1j * Z_c * math.sin(kl)], [1j / Z_c * math.sin(kl), math.cos(kl)]])

      T = np.matmul(T_tube, T)

    Z = (T[0, 0] * Z_rad + T[0, 1]) / (T[1, 0] * Z_rad + T[1, 1])
    Z_in.append(Z)

  Z_mag = []
  for z in Z_in :
    Z_mag.append(20 * math.log10(abs(z)))

  plt.ylim(0, 150)
  plt.plot(freq, Z_mag)
  plt.savefig("simple_cylinder.png")
  plt.show()

if __name__ == "__main__" :
    main()