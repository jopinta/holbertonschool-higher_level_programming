#!/usr/bin/node

const Rectangle = require('./4-rectangle');
// Here, it calls the parent class's constructor with lengths
// provided for the Rectangle's width and height
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
