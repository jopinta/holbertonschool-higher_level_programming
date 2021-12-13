#!/usr/bin/node
// if the first argument can be converted to an integer:
const argv = process.argv;
const integer = parseInt(argv[2]);
// print “Not a number”
if (!integer) {
  console.log('Not a number');
} else {
  console.log('My number: ' + integer);
}
