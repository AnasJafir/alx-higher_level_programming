#!/usr/bin/node
function add(a, b) {
  return a + b;
}
const arg = process.argv.slice(2);
const n1 = parseInt(arg[0]);
const n2 = parseInt(arg[1]);
if (isNaN(n1) || isNaN(n2)) {
  console.log('NaN');
} else {
  const result = add(n1, n2);
  console.log(result);
}
