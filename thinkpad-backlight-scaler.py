#!/usr/bin/env python3

import argparse
import subprocess
import sys


def set_brightness(percent):
  print("Setting brightness to", percent, "%")
  subprocess.run(["xbacklight", "-set", str(percent)])

levels = [
  0,
  1,
  2,
  3,
  4,
  8,
  15,
  25,
  45,
  70,
  100,
]

def clamp_level(l):
  return min(max(l, 0), len(levels)-1)

def set_brightness_level(level):
  set_brightness(levels[clamp_level(level)])

def closest_level_index(brightness):
  return min(range(len(levels)), key=lambda i: abs(brightness-levels[i]))

def get_brightness():
  return float(subprocess.check_output(["xbacklight"]))

def get_brightness_level():
  return closest_level_index(get_brightness())

def main():
  parser = argparse.ArgumentParser(description='Wraps xbacklight, scaling to a few convenient brightness steps')
  parser.set_defaults(mode=None)

  subparsers = parser.add_subparsers()

  parser_inc = subparsers.add_parser('inc', help='increase brightness')
  parser_inc.set_defaults(mode="inc")
  parser_dec = subparsers.add_parser('dec', help='decrease brightness')
  parser_dec.set_defaults(mode="dec")

  args = parser.parse_args()

  if args.mode is None:
    subprocess.run(["xbacklight"])

  elif args.mode == "inc":
    set_brightness_level(get_brightness_level()+1)
  elif args.mode == "dec":
    set_brightness_level(get_brightness_level()-1)
  else:
    sys.stdout.write("Invalid mode\n")
    sys.exit(1)


if __name__ == '__main__':
  main()
