#!/usr/bin/node

import { argv } from 'node:process';

const numOfOccurences = parseInt(argv[2]);

if (isNaN(numOfOccurences)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < numOfOccurences; i++) {
    console.log('C is fun');
  }
}
