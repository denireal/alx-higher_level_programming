#!/usr/bin/node
const sizeInput = parseInt(process.argv[2]);
if (isNaN(sizeInput)) {
    console.log('Missing size');
} else {
    for (let row = 0; row < sizeInput; row++) {
	console.log('X'.repeat(sizeInput));
    }
}
