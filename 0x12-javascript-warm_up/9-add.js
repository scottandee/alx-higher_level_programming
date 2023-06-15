#!/usr/bin/node
// Tjdi script adds the first 2 command line arguments

function add (a, b) {
  return a + b;
}

const a = Number(process.argv[2]);
const b = Number(process.argv[3]);

console.log(add(a, b));
