#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const dict = {};

request(url, function (err, data, body) {
  if (err) {
    console.log(err);
  } else {
    const response = JSON.parse(body);

    for (let i = 0; i < response.length; i++) {
      if (response[i].completed === true) {
        if (dict[response[i].userId] === undefined) {
          dict[response[i].userId] = 1;
        } else {
          dict[response[i].userId] += 1;
        }
      }
    }
  }
  console.log(dict);
});
