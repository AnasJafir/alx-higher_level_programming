#!/usr/bin/node
const fs = require('fs');
let content = process.argv[3];
if (content.startsWith('"') && content.endsWith('"')) {
  content = content.slice(1, -1);
}
fs.writeFile(process.argv[2], content, (err) => {
  if (err) {
    console.log(err);
  }
});
