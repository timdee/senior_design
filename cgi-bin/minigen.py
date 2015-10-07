#! /usr/bin/python2.7

import spidev

# Designed to provide some of the functionality from SparkFun_MiniGen.cpp
class minigen:
  # initialize the connection with the minigen
  def __init__(self):
    self.spi = spidev.SpiDev()
    self.spi.open(0, 0)
    
    self.reset()

  # reset the minigen to a known state
  def reset(self):
    default_frequency = self.frequency_calculation(100.0)

    # set the values of the config registers
    self.config_register = 0x0000

    # set the minigen to the default frequency
    adjust_frequency(default_frequency)

  # Right now this only does sine
  def set_mode(mode='sine'):
    # set the minigen to produce sine wave
    if mode == 'sine':
      pass

  def select_frequency_reg(self, reg):
    pass

  def select_phase_reg(self, reg):
    pass

  def set_frequency_adjust_mode(self, new_mode):
    pass

  def adjust_phase_shift(self, reg, new_phase):
    pass

  # set the minigen to the new_frequency
  def adjust_frequency(self, reg, new_frequency):
    pass

  def close_connection(self):
    self.spi.close()

  # addording to the documentation the output is 
  # fclk / 2^28 * FREQREG
  # fclk set to 16 Mhz (we may need to change this)
  def frequency_calculation(self, desired_frequency ):
    return desired_frequency / .0596


# Test function
def main():
  print 'running in test mode'
  m = minigen()

  print m.frequency_calculation(100.0)

if(__name__ == "__main__"):
  main()
