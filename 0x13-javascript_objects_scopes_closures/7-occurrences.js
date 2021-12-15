#!/usr/bin/node
// number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let aux = 0;

  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      aux++;
    }
  }
  return (aux);
};
