#!/usr/bin/node
// Compute the number of tasks completed by all users

const request = require('request');

const todosUrl = process.argv[2];
const userUrl = 'https://jsonplaceholder.typicode.com/users';

let numOfUsers = 0;

// Query the users url to get list of all users
request(userUrl, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else {
    // Count number of Users
    numOfUsers = JSON.parse(body).length;
  }
});

// Quers the todos url to get an array of all tasks for every user
request(todosUrl, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else {
    const obj = {};
    const arr = JSON.parse(body);

    // Iterate through all userIds
    for (let id = 1; id <= numOfUsers; id++) {
      // Filter the number of 'done' tasks for the user id
      const arrOfDoneByUser = arr.filter(task => {
        return task.completed === true && task.userId === id;
      });
      const numOfDone = arrOfDoneByUser.length;

      // Add the userId and its corresponding number of done tasks to object
      obj['' + id] = numOfDone;
    }
    console.log(obj);
  }
});
