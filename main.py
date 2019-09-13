import random
import sys
import time
from os import system

import argparse

parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(description='Sample usage:  \
        python main.py -n 50 -s 50 -f "x" -p 0.3 -G')

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

args = parser.parse_args()


# Define parameter
TOTAL_STEPS = args.TOTAL_STEPS
FROG_SYMBOL = args.FROG_SYMBOL
SLEEP = args.SLEEP # Amount of sleep time for between each jump
TUI = False # Run the simulation one by one

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
      # print(f'Frog {self.id} reached in {self.jump_taken} steps')
      # self.gen_hist()

  def simulate_jump(self):
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

    sys.stdout.write(pad)
    print('')



average_jumps = 0

all_frogs = []

for frog_id in range(TOTAL_FROGS):
  system('clear')
  frog = Frog(id=frog_id)
  all_frogs.append(frog)

  while not frog.reached:
    max_jump = TOTAL_STEPS - frog.location
    jump_step = random.randint(1, max_jump)
    frog.jump(jump_step)

  average_jumps += frog.jump_taken


average_jumps = average_jumps/TOTAL_FROGS

print(f'\nThe number of average jumps is: {average_jumps}')


histogram = [0] * TOTAL_STEPS
for frog in all_frogs:
  frog.gen_hist()


  for loc in frog.jump_history:
    histogram[loc-1] += 1

print('\nFrog jumping histogram:')
print(histogram)
print('Favourite lily pad (Exluding start & end): ',
        histogram.index(max(histogram[1:-1]))+1)




