#!/usr/bin/node
//computes and prints a factorial

const argv = process.argv;
const nb = parseInt(argv[2]);

function factorial {
  if (nb === 0 || Number.isNaN(nb)) {
    return 1;
  }
return nb * factorial(nb1);
}
console.log(factorial(nb));
