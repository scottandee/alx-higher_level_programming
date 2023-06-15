#!/usr/bin/node
// This script converts the first command line
// argument into a string if it can be converted

const value = parseInt(process.argv[2]);

if (isNaN(value)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + value);
}
