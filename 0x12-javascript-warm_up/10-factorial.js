#!/usr/bin/node
// This script finds the factorial of the command
// line argument passed

import { argv } from 'node:process';

function factorial (a) {
  if (a === 1 || isNaN(a)) {
    return 1;
  }

  return a * factorial(a - 1);
}

const a = Number(argv[2]);
console.log(factorial(a));
