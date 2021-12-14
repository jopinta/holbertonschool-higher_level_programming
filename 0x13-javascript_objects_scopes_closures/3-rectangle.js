#!/usr/bin/node
// empty class
const Rectangle = class {
  constructor (width, height) {
    if (width <= 0 || width === undefined || height <= 0 || height === undefined) {
      return;
    }
    this.width = width;
    this.height = height;
  }

  print () {
    let y = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        y += 'X' + '';
      }
      if (i < this.height - 1) {
        y += '\n';
      }
    }
    console.log(y);
  }
};
module.exports = Rectangle;
