#! /usr/bin/python2.7

import spidev

# connect and talk to the digital pot with spi
# datasheet:
# http://ww1.microchip.com/downloads/en/DeviceDoc/22060b.pdf
class digital_pot:
  # initialize the connection
  def __init__(self):
    self.spi = spidev.SpiDev()
    
    # this should use the second chip enable pin
    self.spi.open(0, 1)

    # according to the datasheet, driving with 2.7v or higher you can use 10mhz
    self.spi.max_speed_hz = 10000000

    self.reset()

  # set the device to a known state
  def reset(self):
    pass

  # set the resistance of the pot.
  # resistance is measured in ohms
  def set_resistance(self, resistance):
    pass

  # close the spi connection
  def close_connection(self):
    self.spi.close()

# Test function
def main():
  print 'running in test mode'
  dp = digital_pot()

  dp.set_resistance(1000)

  dp.close()

if(__name__ == "__main__"):
  main()
