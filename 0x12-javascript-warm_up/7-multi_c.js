#!/usr/bin/node
const numOccurrences = parseInt(process.argv[2]);
if (isNaN(numOccurrences)) {
    console.log('Missing number of occurrences');
} else {
   for (let count = 0; count < numOccurrences; count++) {
       console.log('C is fun');
    }
}
