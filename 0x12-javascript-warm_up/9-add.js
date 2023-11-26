#!/usr/bin/node
// prints the addition of 2 integers

if (process.argv.length !== 4) {
    console.error('Usage: ./script.js <integer1> <integer2>');
    process.exit(1);
}

function add(a, b) {
    return parseInt(a) + parseInt(b);
}

console.log(add(process.argv[2], process.argv[3]));
