#!/usr/bin/node
// converts a number from base 10 to another base

exports.converter = function (base) {
  function convertion (number) {
    return number.toString(base);
  }
  return (convertion);
};
