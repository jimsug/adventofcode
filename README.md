# adventofcode

## 2020

### Day 1

#### Parts A and B

Not too bad, I suppose it's meant to ease you in.

`itertools.combinations` is your friend.

### Day 2

Bitwise `^` is nice! Also, lazy `re` matches, I guess 😉

### Day 3

Not 3 bad :L

Umm... not a lot to say here, except that there might be an O(n) way of doing this?

### Day 4

More sensible part 2 would have included some error handling, but let's assume the input is well-formed...

### Day 5

I suppose we should check that each max/min range is equal after iterations, but this worked `/shrug`

### Day 6

List comprehension worked a treat for the first part.

The second slightly, but not too much more, complicated. I don't know how efficient it is, though.

### Day 7

Hoo, boy. Recursion! Much happier with part two than one.

### Day 8

Probably slightly easier than Day 7, in my estimation. I also misunderstood the instructions for part two slightly, which cost me a lot of time.

### Day 9

`itertools` almost feels like cheating, but I'd be able to implement this without it. It'd just be harder 😛

### Day 10

Dynamic programming is fun, and this was definitely the most challenging so far. Very cool, though.

### Day 11

Oh boy, [day 11.py](adventofcode/2020/day_11/day11.py) is basically a war crime, but I got there in the end.

Main issues were:

* Probably not reading through instructions correctly
* Probably not testing my code against the provided sample early enough (though in my defence, I've been right in the past without really doing this whole 'testing' thing)

I will probably try to clean this up, since it seems to me that part 2, particularly, is potentially problematic in terms of runtime for extremely large input.

### Day 12

So, seems like I'm in a pattern of using a single file for both parts. Makes sense unless (and maybe even if) the input changes between the parts, though.

This is a very naive approach, which I'm sure could be improved.

### Day 13

Hoo, boy.

Part 1 was painful. I couldn't have done part 2 without reddit and way too much learning about Chinese Remainder Theorem. I'm sure it'll come in handy some other time, riiiiight?

### Day 14

So again, firstly, misunderstood part one at first. Then I misunderstood part two at first.

Then I used the wrong method from `itertools`.

But, eventually, I got there, by hook and by crook.

### Day 15

My original implementation of it was pretty naive and is roughly what [day_15.py](adventofcode/2020/day_15/day_15.py) is.

My flatmate suggested parallel arrays, which is what [day_15b.py](adventofcode/2020/day_15/day_15b.py) is, which turns out to be a bit faster even with a reasonably sparse array.

```bash
$ time python3 day_15.py
Part 1 (2020th item): 1015
Part 2 (30000000th item): 201

real	0m18.774s
user	0m18.309s
sys	0m0.460s
$ time python3 day_15b.py
Part 1 (2020th item): 1015
Part 2 (30000000th item): 201

real	0m13.926s
user	0m13.580s
sys	0m0.345s
```

A modest improvement, but an improvement nonetheless.
