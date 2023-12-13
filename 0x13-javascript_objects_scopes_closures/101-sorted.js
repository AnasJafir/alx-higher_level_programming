#!/usr/bin/node
const { dict } = require('./101-data');
const idBYoccur = {};
for (const id in dict) {
  const occur = dict[id];
  if (!idBYoccur[occur]) {
    idBYoccur[occur] = [id];
  } else {
    idBYoccur[occur].push(id);
  }
}
console.log(idBYoccur);
