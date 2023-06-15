#!/usr/bin/node

const numbers = [];
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log('0');
} else {
  for (let i = 2; i < process.argv.length; i++) {
    numbers.push(process.argv[i]);
  }
  numbers.sort(function (a, b) {
    return a - b;
  });
  console.log(numbers[numbers.length - 2]);
}
