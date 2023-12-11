#!/usr/bin/node
const arg = process.argv.slice(2).map(Number);
const numArg = arg.length;
if (numArg <= 1) {
  console.log(0);
} else {
  const sortedArg = Array.from(new Set(arg)).sort((a, b) => b - a);
  console.log(sortedArg[1]);
}
