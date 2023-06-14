#!/usr/bin/node
// This script prints a square of specified size

import { argv } from 'node:process';

const size = parseInt(argv[2]);
let width;

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    width = '';
    for (let j = 0; j < size; j++) {
      width = width + 'X';
    }
    console.log(width);
  }
}
