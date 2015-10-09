#! /usr/bin/python2.7

import spidev
import minigen
import voltage_regulator

#Designed to communicate with a Minigen connected to the GPIO pins
spi = spidev.SpiDev()

# Test function
def main():
  print 'running in test mode'

  # Test setting the frequency using spi
  update_frequency(100)

  # Test setting the voltage using I2c
  update_voltage(5)


# Update the voltage level to the specified value.
# This is not the voltage output by the minigen,
# Instead it is the voltage output by the circuit as a whole.
def update_voltage(voltage):
  #print 'voltage updated'

  # make an instance of the voltage_regulator class to handle the connection
  vr = voltage_regulator()

  # ask vr to set the voltage to the given value
  #vr.set_voltage(voltage)

  # preform cleanup actions
  vr.close_regulator()

# Update the frequency to the specified value. Values are given in Khz.
def update_frequency(frequency):
  #print 'frequency updated'

  # make an instance of the minigen class to handle the connection
  m = minigen()

  # ask the minigen to set the new frequency
  m.set_frequency(frequency)

  #close the conection
  m.close_connection()

if(__name__ == "__main__"):
  main()
