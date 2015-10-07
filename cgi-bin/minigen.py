#! /usr/bin/python2.7

import spidev

# Designed to provide some of the functionality from SparkFun_MiniGen.cpp
spi = spidev.SpiDev()

# Test function
def main():
  print 'running in test mode'

# reset the minigen to a known state
def reset():
  # use the spi interface to communicate with the minigen
  spi.open(0, 0)

  # TODO
  to_send = []

  # perform the transfer and close the conection
  spi.xfer(to_send)
  spi.close()

def set_mode():
  pass

def select_frequency_reg(reg):
  pass

def select_phase_reg(reg):
  pass

def set_frequency_adjust_mode(new_mode):
  pass

def adjust_phase_shift(reg, new_phase):
  pass

def adjust_frequency(reg, mode, new_frequency):
  pass

# addording to the documentation the output is 
# fclk / 2^28 * FREQREG
# fclk set to 16 Mhz (we may need to change this)
def frequency_calculation( desired_frequency ):
  return desired_frequency / .0596

if(__name__ == "__main__"):
  main()
