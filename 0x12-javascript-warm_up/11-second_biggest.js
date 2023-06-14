#!/usr/bin/node

import { argv } from 'node:process';

const numbers = [];
if (argv.length === 2 || argv.length === 3) {
  console.log('0');
} else {
  for (let i = 2; i < argv.length; i++) {
    numbers.push(argv[i]);
  }
  numbers.sort(function (a, b) {
    return a - b;
  });
  console.log(numbers[numbers.length - 2]);
}
