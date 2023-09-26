#!/usr/bin/node
// Print the title of Star Wars movie based
// on the value of id passed as argument

const request = require('request');

const id = process.argv[2];
const api = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(api, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const obj = JSON.parse(body);
    console.log(Object.values(obj)[0]);
  }
});
