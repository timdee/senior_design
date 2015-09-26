#! /usr/bin/python2.7

# This script is designed to test the other python scripts
def main():
  test_suite = Tests()

  print "beginning test suite:"
  test_suite.test1()


class Tests:
  def test1(self):
    print "test1"


if __name__ == '__main__':
  main()
