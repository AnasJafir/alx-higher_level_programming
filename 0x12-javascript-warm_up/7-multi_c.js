#!/usr/bin/node
const arg = process.argv.slice(2);
const num = parseInt(arg[0]);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < num; i++) {
  console.log('C is fun');
}
