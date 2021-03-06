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
* ask user OK/Cancel question ```confirm("text");```
* ask "open" question ```prompt("the question", "text user starts with");```

### Control Flow
* if ... else if ... else ...
* while loops
```Javascript
while (bool) {
  statements here;
}
```
* do loops
```Javascript
do {
  statements;
} while (bool);
```
* for loops
```Javascript
for (var variable = 0; variable < 10; variable = variable + 2){
  statements;
}
```
* breaking out of loop: ```break``` jumps immediately out of enclosing loop
* ```continue``` jumps out of the body and continues with the loop's next iteration
* switch construct
```Javascript
switch (prompt("some question")) {
  case "1":
    statements;
    break;
  case "2":
    statements; // also runs the next case because no break
  case "3":
    statements;
    break;
  default:
    statements;
    break;
}
```

### Updating Variables Succinctly
* use ```+=``` or ```-=``` or ```*=```
* incremental: use ```++``` or ```--```

### Comments
* for single-line comments, use ```//```
* for sections, use ```/* blah blah blah */```

## Functions
* wrapping a piece of program in a value

### Defining a Function
* function definition is a regular variable definition
```Javascript
var square = function(x) {
  return x * x;
}
```
* a ```return``` keyword without an expression after causes function to return ```undefined```

### Parameters and Scopes
* parameters to function behave like regular variables but initial values are given by *caller* of the function
* variables created inside of function are *local* to the Function
* variables declared outside of functions are *global*, as they are visible throughout the program

### Nested Scope
* functions can be created inside of other functions
* **lexical scoping:** variables from block around function's definition are visible, function bodies that enclose it are at top level of program
* in Javascript, the only things that create a new scope are functions
* ```let``` creates a variable that is local to the enclosing *block* not the enclosing *function*

### Functions as Values
* function variables act as names for a specific piece of the program
* function values can do all the other things that other values can do (use in arbitrary expression, store function value in new place, pass as an argument to function, etc)

### Declaration Notation
```Javascript
function square(x) {
  return x * x;
}
```
* works even if function is defined code that uses it
* however cannot put such a function definition inside a conditional block/loop (use function expression)

### The Call Stack
* computer stores the context of flow of control of program in *call stack*
* every time a function is called, the current context is put on the top of the "stack"
* when the function returns, it removes the top context from the stack and continues execution

### Optional Arguments
* if pass a function too many arguments, the extra ones are ignored
* if pass a function too few, the missing parameters are assigned the value ```undefined```
* good for taking in "optional" arguments; if there aren't enough arguments passed then if it's ```undefined```, assign the default value

### Closure
* **closure:** being able to reference a specific instance of local variables in enclosing function
* a closure is a function that "closes over" some local variables
```Javascript
function multiplier(factor) {
  return function(number) {
    return number * factor;
  };
}

var twice = multiplier(2);
console.log(twice(5));
// → 10
```

### Recursion
* function that calls itself

### Growing Functions
* avoid writing very similar code multiple times
* find some functionality haven't written yet and deserves its own function

### Functions and Side Effects
* functions can be divided into those that are called for the *side effects* and the ones that are called for their *return values* (though it's possible to have both)
* **pure function:** value-producing function that not only has no side effects but also doesn't rely on side effects from other code
  * always produces the same value with the same arguments

## Data Structures: Objects and Arrays
* objects allow for grouping values together and building more complex structures

### Data Sets
* **array:** list of values between square brackets, separated by commas
* look up elements by the *indices*

### Properties
* there are expressions that access a *property* of some value
* almost all JS values have properties with the exceptions of ```null``` and ```undefined```
* access properties: using a dot and using square brackets
* dot: part after dot must be valid variable name, directly names the property
* square brackets: expression between brackets is evaluated to get property name

### Methods
* examples: ```thing.push()```, ```thing.toUpperCase()```

### Objects
* **object:** arbitrary collection of properties; can add or remove properties as desired
* to create an object, we can use curly brace notation
* within the curly braces, a list of properties is given separated by commas
```Javascript
var day1 = {
  squirrel: false,
  events: ["work", "touched tree", "pizza", "running",
           "television"]
};
console.log(day1.squirrel);
// → false
console.log(day1.wolf);
// → undefined
day1.wolf = false;
console.log(day1.wolf);
// → false
```
* **binary ```in``` operator:** returns Boolean value that indicates whether object has particular property

### Mutability
* **immutable:** impossible to change value (types: numbers, strings, Booleans)
* Javascript's ```==``` operator only returns ```true``` if two objects are precisely the same value (meaning that they are the same object and have identical contents)
