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

Oh boy, [adventofcode/2020/day_11/day11.py](day 11) is basically a war crime, but I got there in the end.

Main issues were:

* Probably not reading through instructions correctly
* Probably not testing my code against the provided sample early enough (though in my defence, I've been right in the past without really doing this whole 'testing' thing)

I will probably try to clean this up, since it seems to me that part 2, particularly, is potentially problematic in terms of runtime for extremely large input.
