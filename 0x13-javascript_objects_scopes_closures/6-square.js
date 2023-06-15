#!/usr/bin/node

const SquarePrev = require('./5-square');

class Square extends SquarePrev {
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
