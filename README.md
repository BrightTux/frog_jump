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

Sample output from: `python main.py -n 1000 -s 10`

1000 frogs jumping over 10 lily pads.
```
סּ _ _ סּ _ _ _ _ _ סּ
סּ סּ _ _ _ _ _ _ סּ סּ
סּ _ סּ _ _ _ _ _ _ סּ
סּ _ _ סּ _ _ סּ סּ _ סּ
סּ _ _ _ _ סּ _ סּ _ סּ
סּ _ _ _ _ סּ _ _ סּ סּ
סּ _ _ _ _ סּ סּ _ _ סּ
סּ _ _ _ _ _ _ סּ _ סּ
סּ _ _ סּ _ _ _ _ _ סּ
סּ _ _ סּ _ _ _ סּ _ סּ
סּ _ _ _ סּ _ סּ _ _ סּ
סּ _ _ _ סּ סּ _ _ _ סּ
סּ סּ _ _ _ _ _ _ _ סּ
סּ _ _ _ _ _ _ סּ סּ סּ
סּ סּ _ _ _ _ _ _ _ סּ
סּ _ סּ _ _ _ _ סּ סּ סּ
סּ _ _ _ _ _ _ סּ _ סּ
סּ _ _ _ _ סּ סּ _ _ סּ
סּ _ _ _ סּ _ _ _ סּ סּ
סּ _ _ _ _ סּ _ סּ סּ סּ
סּ _ _ _ _ _ _ _ _ סּ
סּ _ _ _ _ סּ _ _ סּ סּ
סּ _ _ _ _ _ _ _ _ סּ
סּ _ _ _ _ _ _ _ סּ סּ
סּ _ _ _ סּ _ סּ _ _ סּ
סּ _ _ _ סּ סּ _ _ _ סּ
סּ _ סּ _ _ _ _ _ סּ סּ
סּ _ סּ _ _ _ _ _ _ סּ
סּ _ סּ _ סּ _ _ _ סּ סּ
סּ _ _ _ _ _ _ _ _ סּ
סּ סּ _ _ _ _ _ _ סּ סּ
סּ _ _ _ _ _ _ _ סּ סּ
סּ _ _ _ _ _ _ סּ _ סּ
סּ _ _ _ _ _ _ סּ סּ סּ
סּ סּ _ _ _ _ _ _ _ סּ
סּ _ _ סּ סּ _ _ _ _ סּ
סּ _ סּ _ _ _ _ סּ סּ סּ
סּ _ _ _ _ _ סּ סּ סּ סּ
סּ _ _ _ _ _ _ סּ סּ סּ
סּ _ _ _ סּ _ סּ _ סּ סּ
סּ _ _ _ _ _ _ סּ _ סּ
סּ _ _ _ _ _ _ סּ _ סּ
סּ _ _ _ _ _ _ סּ סּ סּ
סּ _ _ _ סּ סּ _ _ _ סּ
סּ _ _ _ _ סּ סּ סּ _ סּ
סּ _ _ _ _ _ _ _ _ סּ
סּ _ _ סּ _ _ סּ _ סּ סּ
סּ _ _ _ _ סּ _ סּ סּ סּ
סּ _ _ _ _ _ _ סּ סּ סּ
סּ _ סּ _ _ _ _ סּ סּ סּ
סּ _ _ סּ _ _ _ _ _ סּ
סּ _ _ סּ _ _ סּ סּ _ סּ
סּ _ _ _ _ סּ _ סּ סּ סּ
סּ _ _ _ _ _ _ _ _ סּ
סּ _ סּ _ _ _ _ סּ סּ סּ
סּ _ _ _ _ _ _ סּ סּ סּ

Frog jumping histogram:
[1000, 91, 115, 144, 167, 204, 241, 323, 476, 1000]
Favourite lily pad (Exluding start & end):  9
```
