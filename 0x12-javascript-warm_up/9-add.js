#!/usr/bin/node
const firstNumber = parseInt(process.argv[2]);
const secondNumber = parseInt(process.argv[3]);
function add (num1, num2) {
    if (isNaN(num1) || isNaN(num2)) {
	    return NaN;
    }
    return num1 + num2;
}
console.log(add(firstNumber, secondNumber));
