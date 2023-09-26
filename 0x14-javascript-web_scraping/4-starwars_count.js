#!/usr/bin/node
// This script prints the number of movies where
// the character 'Wedge Antilles' with an id of
// 18 is present

const request = require('request');

const url = process.argv[2];
const wedgeUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else {
    // convert json to object
    const obj = JSON.parse(body);

    let count = 0;
    for (let i = 0; i < obj.count; i++) {
      // Get the array characters in present in the movie
      const characters = obj.results[i].characters;

      // Check if Wedge Antilles is present
      if (characters.includes(wedgeUrl)) {
        count += 1;
      }
    }
    console.log(count);
  }
});
