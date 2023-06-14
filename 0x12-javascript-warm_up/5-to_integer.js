#!/usr/bin/node
// This script converts the first command line
// argument into a string if it can be converted

import { argv } from 'node:process';

const value = parseInt(argv[2]);

if (isNaN(value)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + value);
}
