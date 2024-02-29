// Task 1: Add two numbers
int addTwo(int a, int b) {
  return a + b;
}

// Task 2: Subtract two numbers
int subtractTwo(int a, int b) {
  return a - b;
}

// Task 3: Multiply two numbers
int multiplyTwo(int a, int b) {
  return a * b;
}

// Task 4: Divide two numbers
double divideTwo(double a, double b) {
  if (b != 0) {
    return a / b;
  } else {
    throw ArgumentError('Cannot divide by zero');
  }
}

// Task 5: Get the length of a string
int stringLength(String str) {
  return str.length;
}

// Task 6: Get the first element of a list
dynamic getFirstElement(List<dynamic> list) {
  if (list.isNotEmpty) {
    return list[0];
  } else {
    throw ArgumentError('List is empty');
  }
}

void main() {
  // Testing the functions
  print(addTwo(5, 3)); // Output: 8
  print(subtractTwo(10, 4)); // Output: 6
  print(multiplyTwo(7, 2)); // Output: 14
  print(divideTwo(10, 2)); // Output: 5.0
  print(stringLength('Hello')); // Output: 5
  print(getFirstElement([1, 2, 3])); // Output: 1
}
