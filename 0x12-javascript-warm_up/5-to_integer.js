#!/usr/bin/node
// This script converts the first command line
// argument into a string if it can be converted

import { argv } from 'node:process';

const value = Number(argv[2]);

if (isNaN(value)) {
  console.log('No arguments');
} else {
  console.log('My number: ' + value);
}
