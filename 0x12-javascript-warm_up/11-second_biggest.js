#!/usr/bin/node

let numbers = process.argv.slice(2).map((x) => {
    return parseInt(x);
});

if (numbers.length <= 1) {
    console.log(0);
} else {
    console.log(numbers.sort((a, b) => {
        return b - a;
    })[1]);
}
