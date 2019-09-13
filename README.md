# This repo was made for fun.

### Average frog jumps challenge.
The problem is as such - 

Assuming there are 8 lily pads between the 2 river bank.
* The frog can only jump in 1 direction.
* The frog can jump `n` number of steps using `range(1, other_bank_location - current_postion)`
* Each of the remaining lily pads has an equal chance for the frog to jump unto

#### Example:
* If the frog's current position is at the starting river bank, 
the frog can jump either 1,2,3,4,...,9 steps until it reaches the other river bank.

#### Question:
What is the average number of jumps required to reach the other side of the river bank?

Sample output from: `python main.py -n 10 -s 10 -H`

10 frogs jumping over 10 lily pads.
```
סּ _ _ _ _ _ סּ _ סּ סּ   |  Frog ID: 0
סּ _ סּ _ _ _ _ סּ _ סּ   |  Frog ID: 1
סּ _ _ סּ סּ סּ _ _ _ סּ   |  Frog ID: 2
סּ _ _ סּ _ _ _ _ _ סּ   |  Frog ID: 3
סּ _ _ _ _ _ _ סּ _ סּ   |  Frog ID: 4
סּ _ _ _ _ _ סּ סּ סּ סּ   |  Frog ID: 5
סּ _ _ _ _ סּ סּ _ סּ סּ   |  Frog ID: 6
סּ _ סּ _ _ סּ _ סּ _ סּ   |  Frog ID: 7
סּ _ _ _ _ סּ סּ סּ _ סּ   |  Frog ID: 8
סּ _ _ _ סּ סּ _ סּ _ סּ   |  Frog ID: 9

-> A total of **10** frogs jumped!
   The number of average jumps is: 3.4 for 10 lily pads

   Frog jumping histogram:
   [10, 0, 2, 2, 2, 5, 4, 6, 3, 10]

   Favourite lily pad (Exluding start & end):  8

   Normalized Histogram:
    2 |
    3 | סּסּסּסּסּסּסּסּסּסּסּסּסּ
    4 | סּסּסּסּסּסּסּסּסּסּסּסּסּ
    5 | סּסּסּסּסּסּסּסּסּסּסּסּסּ
    6 | סּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּ
    7 | סּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּ
    8 | סּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּ
    9 | סּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּסּ

```

#### Usage:
```
usage: main.py [-h] [-s TOTAL_STEPS] [-n TOTAL_FROGS] [-f FROG_SYMBOL]
               [-p SLEEP] [-G] [-H]

Sample usage: python main.py -n 50 -s 50 -f "סּ" -p 0.3 -G

optional arguments:
  -h, --help            show this help message and exit
  -s TOTAL_STEPS, --TOTAL_STEPS TOTAL_STEPS
                        Total jump steps
  -n TOTAL_FROGS, --TOTAL_FROGS TOTAL_FROGS
                        Total frog samples
  -f FROG_SYMBOL, --FROG_SYMBOL FROG_SYMBOL
                        Symbol used to represent frogs
  -p SLEEP, --SLEEP SLEEP
                        Only applicable if simulation of frog jumping is
                        desired
  -G, --TUI             if '-G' is provided, simulation of frogs jumping will
                        be displayed
  -H, --HISTORY         if '-H' is provided, the frog jumping history will be
                        printed
```

