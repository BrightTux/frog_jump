import random
import sys
import time
from os import system

import argparse

parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(description='Sample usage:  \
        python main.py -n 50 -s 50 -f "סּ" -p 0.3 -G')

parser.add_argument("-s", "--TOTAL_STEPS", type=int, help='Total jump steps',
        default=10)
parser.add_argument("-n", "--TOTAL_FROGS", type=int, help='Total frog samples',
        default=100)
parser.add_argument("-f", "--FROG_SYMBOL", help='Symbol used to represent frogs',
        default='סּ')
parser.add_argument("-p", "--SLEEP", type=float, help='Only applicable if \
        simulation of frog jumping is desired', default=0.3)
parser.add_argument("-G", "--TUI", dest='run_simulator',
                    action='store_true', help="if '-G' is provided, \
                    simulation of frogs jumping will be displayed")
parser.add_argument("-H", "--HISTORY", dest='print_history',
                    action='store_true', help="if '-H' is provided, \
                    the frog jumping history will be printed")

args = parser.parse_args()


# Define parameter
TOTAL_STEPS = args.TOTAL_STEPS
FROG_SYMBOL = args.FROG_SYMBOL
SLEEP = args.SLEEP # Amount of sleep time for between each jump
TUI = False # Run the simulation one by one
KEEP = []

if args.run_simulator:
    TUI = True

TOTAL_FROGS = args.TOTAL_FROGS

class Frog:
  def __init__(self, id=0, jump_taken=0, reached=False, location=1,
      total_steps=TOTAL_STEPS, tui=TUI):
    self.id = id
    self.jump_taken = jump_taken
    self.reached = reached
    self.location = location
    self.total_steps = TOTAL_STEPS
    self.jump_history = [1]
    self.tui = tui

  def jump(self, jump_step):
    if self.tui:
      self.simulate_jump()
    if not self.reached:
      self.jump_taken += 1
      self.location += jump_step
      self.jump_history.append(self.location)

    if self.location == self.total_steps:
      self.reached = True
      if self.tui:
        self.simulate_jump()

  def simulate_jump(self):
    for i in KEEP:
      print(i)
    # generate lily pads
    pad = TOTAL_STEPS*'_ '
    # print frog location:
    pad = list(pad)
    pad[self.location*2 - 2] = FROG_SYMBOL
    pad.append(f' {self.location}\n')

    pad = "".join(pad)
    sys.stdout.write(pad)
    sys.stdout.flush()
    time.sleep(SLEEP)
    system('clear')

  def gen_hist(self):
    pad = TOTAL_STEPS*'_ '
    pad = list(pad)
    for loc in self.jump_history:
      pad[loc*2 - 2] = FROG_SYMBOL
    pad = "".join(pad)

    text = pad + "  |  Frog ID: " + str(self.id)

    sys.stdout.write(text)
    print('')
    KEEP.append(text)

average_jumps = 0

all_frogs = []

for frog_id in range(TOTAL_FROGS):
  frog = Frog(id=frog_id)
  all_frogs.append(frog)

  while not frog.reached:
    max_jump = TOTAL_STEPS - frog.location
    jump_step = random.randint(1, max_jump)
    frog.jump(jump_step)

  average_jumps += frog.jump_taken
  if args.print_history:
    frog.gen_hist()

average_jumps = average_jumps/TOTAL_FROGS
histogram = [0] * TOTAL_STEPS

for frog in all_frogs:
  for loc in frog.jump_history:
    histogram[loc-1] += 1

if args.print_history:
  system('clear')
  for i in KEEP:
    print(i)

print()
print(f'-> A total of **{TOTAL_FROGS}** frogs jumped!')
print(f'   The number of average jumps is: {average_jumps} for {TOTAL_STEPS} '
      f'lily pads \n')
print('   Frog jumping histogram:')
print('  ', histogram, '\n')
print('   Favourite lily pad (Exluding start & end): ',
        histogram.index(max(histogram[1:-1]))+1)

print('\n   Normalized Histogram:', end='')
# normalize the histogram
norm_hist = [(pad/sum(histogram))*300 for pad in histogram]
for idx, hist in enumerate(norm_hist):
  if idx != 0 and idx != len(histogram)-1:
    print('{:>5}'.format(idx+1), end='')
    print(" | ", end='')

    for i in range(int(norm_hist[idx])):
      print('סּ', end='')

  print('')




