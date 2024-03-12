#!/usr/bin/node

const fs = require('fs');

const sourceFilePath1 = process.argv[2];
const sourceFilePath2 = process.argv[3];
const destinationFilePath = process.argv[4];

function appendFileContentsToDestination(err, data) {
  if (err) {
    return console.error(err);
  }

  fs.appendFile(destinationFilePath, data, function (err) {
    if (err) console.error(err);
  });
}

fs.readFile(sourceFilePath1, 'utf8', appendFileContentsToDestination);
fs.readFile(sourceFilePath2, 'utf8', appendFileContentsToDestination);
