#!/usr/bin/node

const originalDictionary = require('./101-data').dict;
const sortedDictionary = {};

Object.keys(originalDictionary).forEach(key => {
  const originalValue = originalDictionary[key];
  if (sortedDictionary[originalValue] === undefined) sortedDictionary[originalValue] = [];
  sortedDictionary[originalValue].push(key);
});

console.log(sortedDictionary);
