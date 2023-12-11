#!/usr/bin/node
const arg = process.argv.slice(2);
const num = parseInt(arg[0]);

if (!isNaN(num)) {
  console.log(num);
} else {
  console.log('Not a number');
}
