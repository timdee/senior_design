#! /usr/bin/python2.7

import spidev

#Designed to communicate with a Minigen connected to the GPIO pins
spi = spidev.SpiDev()

# Test function
def main():
  print 'running in test mode'

  # Test setting the frequency using spi
  update_frequency(100)


# Update the voltage level to the specified value.
# This is not the voltage output by the minigen,
# Instead it is the voltage output by the circuit as a whole.
def update_voltage(voltage):
  #print 'voltage updated'
  pass

# Update the frequency to the specified value. Values are given in Khz.
def update_frequency(frequency):
  #print 'frequency updated'

  # use the spi interface to communicate with the minigen
  spi.open(0, 0)

  # compute the bytes to send
  to_send = [0x01, 0x02, 0x03]

  # perform the transfer and close the conection
  spi.xfer(to_send)
  spi.close()

if(__name__ == "__main__"):
  main()
