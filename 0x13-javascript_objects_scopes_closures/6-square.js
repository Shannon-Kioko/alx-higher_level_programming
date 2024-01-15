#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    if (!c) {
      for (let c = 0; c < this.width; c++) {
        console.log('X'.repeat(this.width));
      }
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
// const s1 = new Square(4);
// s1.charPrint();

// s1.charPrint('Z');
module.exports = Square;
