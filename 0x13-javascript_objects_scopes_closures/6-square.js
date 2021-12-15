#!/usr/bin/node
// rectangle using the character c

const Sq = require('./5-square');

module.exports = class Square extends Sq {
  charPrint (c) {
    let y = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        if (c === undefined) {
          y += 'X' + '';
        } else {
          y += c + '';
        }
      }
      console.log(y);
      y = '';
    }
  }
};
