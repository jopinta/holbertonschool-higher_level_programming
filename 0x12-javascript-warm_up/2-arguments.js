#!/usr/bin/node
// prints a message depending of the number of arguments passed
const argv = process.argv.length;

// print process.ar
if (argv <= 2) {
  console.log('No argument');
} else if (argv === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
