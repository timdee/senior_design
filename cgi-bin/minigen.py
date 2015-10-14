#! /usr/bin/python2.7

import spidev
import time

# Designed to provide some of the functionality from SparkFun_MiniGen.cpp
# designed so that you only need to use set_frequency to set the frequency
class minigen:
  # initialize the connection with the minigen
  def __init__(self):
    self.spi = spidev.SpiDev()
    self.spi.open(0, 0)

    self.reset()
   
    #while(True):  
      #self.spi.writebytes([0xAC,0xFF])

  def write_config_register(self):
    # send high bits than low bits
    high_bits = (self.config_register >> 8) & 0xFF
    low_bits = self.config_register & 0xFF

    self.spi.writebytes([high_bits, low_bits])

  # reset the minigen to a known state
  def reset(self):
    # decide on a default frequency to set
    default_frequency = 100.0

    # set the current frequency register
    self.frequency_register = 'freq0'

    # set the values of the config registers
    self.config_register = 0x0000

    # set adjust mode to full
    self.set_frequency_adjust_mode()

    # set the mode to sine
    self.set_mode()

    # set the phase shift of both phase registers to 0
    self.adjust_phase_shift('phase0', 0x0000)
    self.adjust_phase_shift('phase1', 0x0000)

    # set the minigen to the default frequency 
    # doing this twice sets both frequency registers to default_frequency
    self.set_frequency(default_frequency)
    self.set_frequency(default_frequency)

    # I don't know why do this?
    self.spi.writebytes([0x01, 0x00])
    self.spi.writebytes([0x00, 0x00])

  # set the output mode
  def set_mode(self, mode='sine'):
    # clear D5, D3, and D1
    self.config_register &= ~0x002A

    # set the minigen to produce sine wave
    if mode == 'sine':
      self.config_register |= 0x0000
    elif mode == 'triangle':
      self.config_register |= 0x0002
    elif mode == 'square_2':  
      self.config_register |= 0x0020
    elif mode == 'square':
      self.config_register |= 0x0028

    self.write_config_register()

  # there are two frequency registers.
  # freq0, freq1
  # select which frequency register the device should be using
  def select_frequency_reg(self, reg):
    if reg == 'freq0':
      self.config_register &= ~0x0800 
    elif reg == 'freq1':
      self.config_register |= 0x0800

    self.write_config_register()

  # there are two phase registers. 
  # phase0, phase1
  # Select which phase register the device should be using.
  def select_phase_reg(self, reg):
    if reg == 'phase0':
      self.config_register &= ~0x0400
    elif reg == 'phase1':
      self.config_register |= 0x0400

    self.write_config_register()

  # sets the mode for frequency generation.
  # only full mode is provided right now.
  def set_frequency_adjust_mode(self, new_mode='full'):
    if new_mode == 'full':
      self.config_register |= 0x2000

    self.write_config_register()

  def adjust_phase_shift(self, reg, new_phase):
    # clear the top three bits, these denote the phase register
    phase = new_phase & ~0xF000

    if reg == 'phase0':
      phase |= 0xC000
    elif reg == 'phase1':
      phase |= 0xE000

    # send high bits than low bits
    high_bits = (phase >> 8) & 0xFF
    low_bits = phase & 0xFF

    self.spi.writebytes([high_bits, low_bits])    

  # decides how to set the frequency in the minigen
  # does the frequency calculation,
  # then sets the frequency
  def set_frequency(self, new_frequency):
    frequency = self.frequency_calculation(new_frequency)

    # set the values in the frequency register that is not being used
    # set the next frequency register to be the other register
    if(self.frequency_register == 'freq0'):
      # set up 'freq1'
      self.adjust_frequency('freq1', new_frequency)
      self.frequency_register = 'freq1'
    else:
      # set up 'freq0'
      self.adjust_frequency('freq0', new_frequency)
      self.frequency_register = 'freq0'

    # set the minigen to use the frequency register we just set
    self.select_frequency_reg(self.frequency_register)

  # set the minigen to the new_frequency
  # can assume the mode is set to full because that is the only mode we provided
  def adjust_frequency(self, reg, new_frequency):
    # in full mode we write out to two different registers
    # grab the lower 16 bits of new_frequency, clear first 2 bits
    temp_low_bits = (int(new_frequency) & 0xFFFF) & ~0xC000 

    # grab the upper 16 bits of new_frequency, clear first 2 bits
    temp_high_bits = ( (int(new_frequency) >> 14) ) & ~0xC000

    #print new_frequency
    #print temp_low_bits.bit_length()
    #print temp_high_bits.bit_length()

    # set the top two bits based on the reg parameter
    if reg == 'freq0':
      temp_low_bits |= 0x4000
      temp_high_bits |= 0x4000
    elif reg == 'freq1':
      temp_low_bits |= 0x8000
      temp_high_bits |= 0x8000

    # write the low bits out
    # send high bits than low bits
    high_bits = (temp_low_bits >> 8) & 0xFF
    low_bits = temp_low_bits & 0xFF

    print high_bits
    print low_bits

    self.spi.writebytes([high_bits, low_bits])

    # write the high bits out
    # send high bits than low bits
    high_bits = (temp_high_bits >> 8) & 0xFF
    low_bits = temp_high_bits & 0xFF

    self.spi.writebytes([high_bits, low_bits])

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

  #m.set_mode('square')
  m.set_mode('sine')

  m.set_frequency(100)
  time.sleep(5)
  m.set_frequency(100)

  #for i in range(0,20):
   # m.set_frequency(200)
    #time.sleep(3)
  
  #while(True):
  #  m.set_frequency(200)

  #print m.frequency_calculation(100.0)

  m.close_connection()

if(__name__ == "__main__"):
  main()
