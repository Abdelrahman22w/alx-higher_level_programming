#!/usr/bin/node
// prints a message depending on the number of arguments passed

const count = process.argv.length - 2;

if (count < 1) {
    console.log('No argument');
} else if (count === 1) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
