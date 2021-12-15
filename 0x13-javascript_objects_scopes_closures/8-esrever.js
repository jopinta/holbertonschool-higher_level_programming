#!/usr/bin/node
// reverse returns the reversed version of a list

exports.esrever = function (list) {
  const rever = [];
  for (let i = list.length - 1; i >= 0; i--) {
    rever.push(list[i]);
  }
  return (rever);
};
