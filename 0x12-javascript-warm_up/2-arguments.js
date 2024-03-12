#!/usr/bin/node
const numb = process.argv.length - 2;
if (numb === 0) {
    console.log('No argument');
} else if (numb === 1) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
