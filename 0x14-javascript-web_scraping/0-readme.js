#!/usr/bin/node
const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: node readfile.js <file-path>');
  process.exit(1);
}

// Get the file path from command line arguments
const filePath = process.argv[2];

// Read and print the content of the file
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString());
  }
});
