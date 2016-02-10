# Javascript

## Values, Types, Operators
* **types:** numbers, strings, Booleans, objects, functions and undefined values

### Number Values
  * uses 64 bits
  * fractional numbers written using a dot
  * very small or very small number use "e" (for exponent)
  * **arithmetic:** use operators (+ , - , * , / , %)
  * special numbers: ```Infinity```, ```NaN``` (not a number: no precise, meaningful value)

### Strings
* used to represent text, can use single or double quotes
* escape character ```\```
  * ```\t```: tab
  * ```\n```: newline
* can be concatenated using ```+```

### Unary Operators
* only operates on one value (eg. ```typeof```)

### Boolean Values
* ```true``` and ```false```
* need to be put in round brackets
* logical operators ( ```&&``` and ```||```)

### Undefined Values
* ```null``` and ```undefined```

### Automatic Type Conversion
* **type coercion:** JS will convert value to the type that it wants
* converting strings and numbers to Boolean values: 0, NaN and empty string ("") are ```false``` while all other values are ```true```
* ```===``` and ```!==``` tests whether a value is precisely equal to the other so that 0, NaN and empty string ("") do not equal to false

### Short Circuiting of Logical Operators (```&&``` and ```||```)
* the ```||``` operator will return the value to the left when it can be converted to true otherwise it will return the value to its right
* the ```&&``` operator works the other way around; returns the left value if it converts to false otherwise returns the value on its right
* **short-circuit evaluation:** the expression to the right is only evaluated when necessary

## Program Structure
* **expression:** ends with a semicolon
* **side effect:** change internal state of machine in a way that will affect statements that come after it

### Variables
* **variable:** to catch and hold values
```Javascript
var caught = 5 * 5;
```

### Keywords and Reserved Words
* may not be used as variable names

### Environment
* **environment:** collection of variables and their values that exist at given time

### Functions
* **function:** piece of program wrapped in a value, values are given to functions called *arguments*
* ```console.log()``` function used to output values
  * use Command-Option-I to open web console/developer tools
* showing a dialog box or writing text to the screen is a *side effect*
* when a function produces a value, it is said to *return* the value

### Prompt and Confirm
