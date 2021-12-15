#!/usr/bin/node
// prints the number of arguments already printed

let x = 0;
exports.logMe = function (item) {
  console.log(x + ': ' + item);
  x++;
};
