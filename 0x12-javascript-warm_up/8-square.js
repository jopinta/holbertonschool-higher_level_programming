#!/usr/bin/node
// script that prints x times “C is fun”
const argv = process.argv;
const integer = parseInt(argv[2]);

if (isNaN(integer)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < integer; i++) {
    console.log('X'.repeat(integer));
  }
}
