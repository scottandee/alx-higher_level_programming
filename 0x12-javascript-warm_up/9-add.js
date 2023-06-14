#!/usr/bin/node
// Tjdi script adds the first 2 command line arguments

import { argv } from 'node:process';

function add (a, b) {
  return a + b;
}

const a = Number(argv[2]);
const b = Number(argv[3]);

console.log(add(a, b));
