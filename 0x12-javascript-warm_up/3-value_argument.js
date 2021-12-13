#!/usr/bin/node
// prints a message depending of the number of arguments passed
const argv = process.argv;

// print process.ar
if (argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
