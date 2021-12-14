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
};
module.exports = Rectangle;
