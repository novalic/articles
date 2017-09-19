# Math problems

These are some interesting math problems on which I programmed solutions.

## [388.py](/388.py)

This is a nice problem that formed part of my University's math workshops for highschool students:
```
How many numbers of 7 or less digits whose last 3 (digits) are 388 are multiples of 388?
```
It is indeed a really nice mathematical problem.
A quick and easy solution that I figured out and doesn't involve too much theory:

```
The problem asks to find out x digit numbers for x = (3, .. ,7) whose last 3 digits are 388 (and count them).

So for every number x it's easy to see that in the result of: n*10**(number of digits in n) + n ends with the number n and this result is divisible by n.

i.e: 
8*(10 + 1) = 8*10 + 8*1 = 80 + 8 = 88
76*101 = 7600 + 76 = 7676

And in particular 388*1001 = 388388.

So we can formulate it like this:
388*k < 10000000
if we divide by 388 and round up:
k < 25773

So 388*k < 10000000 if k < 25773.

Now, as the prime decomposition of 388 is 2*2*97, we can write 388 as 4*97.
Now 388*1000 = (4*97)*(4*250) so every 250 k's we have a multiple of 388 that ends with three zeros, and if we add 388 to that number, we have found one of the numbers we are looking for.
So now we see how many of this numbers are in the valid range:
25773/250 = 103

So 388*(250*i) for i = (1, ... , 103) are all valid numbers. To end up we need to count the solution obtained by: 388*(250*0) = 388 that we weren't counting (Note that 388*(250*1) = 97000).

Adding up, in total theres 104 numbers seven digits or less whose last three digits are 388 in that order. 
```
To check out the number obtained before I've written this piece of code as concise as possible:

```python
print (len([ x for x in map(lambda n: n[-3:], map(str, [y * 388 for y in range(1, int(10000000/388))])) if "388" in x ]))
```

And the output is as expected :+1: :+1:

Basically what I'm doing is:

- As the smallest 8 number digit is 10000000 we can find out how many multiples of 388 we have that are less than 10000000 by dividing.
- Creating a list of all multiples of 388 in the range 388 and 10000000.
- Using the map function to convert all the elements of this list (which are integers) to strings.
- Defining a lambda function which given an element, returns it's last 3 characters.
- Using the map function with the previous mentioned lambda function on the list resulting of applying the first map function mentioned before.
- Extracting elements from the resulting list of the second map function application, which satisfy that the string "388" is a part of this element.
- We can easily note that this returns a list of elements which are all completely equal strings "388". So we count how many elements are on this list and print the result.
