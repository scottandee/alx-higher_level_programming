#!/usr/bin/node
// This script gets the content of a webpage
// and stores it in a file

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const fileName = process.argv[3];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(fileName, body, 'utf-8', (err) => {
      if (err) console.log(err);
    });
  }
});
