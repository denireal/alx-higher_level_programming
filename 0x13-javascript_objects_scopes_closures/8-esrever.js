#!/usr/bin/node

exports.esrever = function(inputArray) {
  const reversedArray = [];

  for (let index = inputArray.length - 1; index >= 0; index--) {
    reversedArray.push(inputArray[index]);
  }

  return reversedArray;
};
