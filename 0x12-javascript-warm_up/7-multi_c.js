#!/usr/bin/node
// This prints the string 'C is fun' x times.
// x being the number of times to print

import { argv } from 'node:process';

const numOfOccurences = Number(argv[2]);

if (isNaN(numOfOccurences)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < numOfOccurences; i++) {
    console.log('C is fun');
  }
}
