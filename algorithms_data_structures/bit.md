# Bit Manipulation

## Bit Representation

### The Base 2 Number System
* each digit represents a power of two (e.g.|8|4|2|1|)
* represented in python in the form of ```0b#####```

### bin()
* in python, you can use the bin() function that takes in an integer as the argument and returns the base 2 representation of the integer

### int()
* the int() function has a second optional parameter
* it takes in a string and a base and returns that base representation of the integer in the string
```python
int('0b100', 2) # returns 4
int('11001001', 2) # returns 201
```

## Bitwise Operators

### Bit Shift
* left bit shift ```<<```
* right bit shift ```>>```
* mathematically equivalent to floor dividing and multiplying by 2 every time shifted
* it just shifts the digits the direction however many times shifted
* bitwise operators only on integers!
```Python
# Left Bit Shift (<<)  
0b000001 << 2 == 0b000100 # (1 << 2 = 4)
0b000101 << 3 == 0b101000 # (5 << 3 = 40)       
# Right Bit Shift (>>)
0b0010100 >> 3 == 0b000010 # (20 >> 3 = 2)
0b0000010 >> 2 == 0b000000 # (2 >> 2 = 0)
```

### Bitwise AND (```&```) Operator
* returns a number where the bits of that number are turned on if both comparing numbers have 1 at that bit
```python
bin(0b1100 & 0b1001) # outputs 0b1000
```

### Bitwise OR (```|```) Operator
* returns a number where the bits of that number are turned on if either comparing number has a 1 at that bit
```python
bin(0b1100 | 0b1001) # outputs 0b1101
```

### XOR (```^```) Exclusive Or Operator
* returns a number where the bits of that number are turned on if only one of the comparing numbers has a 1 at that bit
```python
bin(0b1100 ^ 0b1001) # outputs 0b101
```

### Bitwise NOT (```~```) Operator
* flips all the bits of a single number
* result: adding one and making the number negative
```python
~123 # outputs -124
```

## More Complex
* **bit mask:** variable that helps with bitwise operations
  * can help turn specific bits on/off or collect data from integer about which bits are on/off
```python
num  = 0b1100
mask = 0b0100
desired = num & mask
if desired > 0:
    print "Bit was on"
```
* can use the OR (```|```) operator to turn on a bit by using a mask with the desired bit to be turned on to be 1
* can flip bits using the XOR (```^```) operator, as using ```^``` on a bit with the number one will return a result where it is flipped
* can use the shift operators (```<<```) and (```>>```) to slide masks into place
