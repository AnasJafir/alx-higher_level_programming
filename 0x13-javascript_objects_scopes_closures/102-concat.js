#!/usr/bin/node
const fs = require('fs');
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
const content1 = fs.readFileSync(fileA, { encoding: 'utf8' });
const content2 = fs.readFileSync(fileB, { encoding: 'utf8' });
const result = `${content1}${content2}`;
fs.writeFileSync(fileC, result, { encoding: 'utf8' });
