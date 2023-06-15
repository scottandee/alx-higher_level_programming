#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let sym = c;
    if (c === undefined) {
      sym = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let width = '';
      for (let j = 0; j < this.width; j++) {
        width = width + sym;
      }
      console.log(width);
    }
  }
}

module.exports = Square;
