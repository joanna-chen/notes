# Swift

## Overview 
```Swift
print("Hello world!") 
var variable = 5
let constant = 10
```

### Casting
```Swift 
word = "Hello World \(constant + variable)" + String(variable)
```

### Arrays and Dictionaries 
```Swift 
list = []
dictionary = [:]
list = [String]()
dictionary = [String: Int]()
var list = [“fish”, “dog”, “cat”]
var dictionary = [list[0]: 3, list[1]: 2, list[2]: 1]
``` 

### Control Flow 
* () around condition optional, but must have {} around body
* **for-in** to iterate through lists and dictionaries
```Swift
for i in list { 
	pass
}
for (x,y) in dictionary { 
	pass
}
```
* **while** loops are normal 

#### Looping a range of indexes 
```Swift 
for i in 0..<4 { 
	print(i) //exclusive top
}
for i in 0...4 {
	print(i) //inclusive top
}
```

#### Switch Case 
* must be exhaustive and have default case
```Swift 
switch (4) {
case let x where x%2==0: 
	print("\(x) is an even number!") //checks if the switch thing is divisible by 2 and makes it x
default: 
	print("it is an odd number")
}
```

### Optionals 
```Swift
var optionalThing: Int? = 5

if let thing = optionalThing { //checks if optionalThing is not nil
	print(thing)
} 
```

### Functions 
```Swift 
func greet(name: String, day: String) -> String { 
	return "Hello \(name), today is \(day)!"
} 
greet("Joanna", day: "Monday") 
```
* functions can return a tuple, whose elements can be referred to by name or number 

* functions can take a variable number of arguments and put them in an array 
```Swift 
func sumOf(numbers: Int...) -> Int { 
	var sum = 0
	for num in numbers { 
		sum += num
	}
	return sum
}
sumOf(1)
sumOf(2, 54, 332)
```

* functions can be nested
* functions are first-class type, function can return another function as value and can also take function in as argument 
* parameters can have an argument label or **_** for no argument label
* 

