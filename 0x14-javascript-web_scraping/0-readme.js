#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf-8', (err, jsonString) => {
  if (err) {
    console.log(err);
  } else {
    console.log(jsonString);
  }
});
