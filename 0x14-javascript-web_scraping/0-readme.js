#!/usr/bin/node
// Read and print the contents of a file

const fs = require('node:fs');

const file = process.argv[2];
fs.readFile(file, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
