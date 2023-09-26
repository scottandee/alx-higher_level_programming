#!/usr/bin/node
/* This script writes a string passed as
argument into a file */

const fs = require('fs');

const filePath = process.argv[2];
const text = process.argv[3];
fs.writeFile(filePath, text, 'utf-8', err => {
  if (err) {
    console.log(err);
  }
});
