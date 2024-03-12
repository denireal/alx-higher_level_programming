#!/usr/bin/node

exports.nbOccurences = function(array, searchElement) {
  let occurrenceCount = 0;

  array.forEach(element => {
    if (element === searchElement) occurrenceCount++;
  });

  return occurrenceCount;
};
