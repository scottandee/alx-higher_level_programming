#!/usr/bin/node
// This script finds the factorial of the command
// line argument passed

function factorial (a) {
  if (a === 1 || isNaN(a)) {
    return 1;
  }

  return a * factorial(a - 1);
}

const a = Number(process.argv[2]);
console.log(factorial(a));
