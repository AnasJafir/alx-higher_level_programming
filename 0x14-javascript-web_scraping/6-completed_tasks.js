#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const todos = JSON.parse(body);
    const completed = {};
    todos.forEach((todo) => {
      if (todo.completed && completed[todo.user_id] === undefined) {
        completed[todo.user_id] = 1;
      } else if (todo.completed) {
        completed[todo.user_id] += 1;
      }
    });
    console.log(completed);
  }
});
