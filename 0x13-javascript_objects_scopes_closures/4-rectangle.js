#!/usr/bin/node
class Rectangle {
  width;
  height;
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let r = 0; r < this.height; r++) {
      let Recty = '';
      for (let c = 0; c < this.width; c++) {
        Recty += 'X';
      }
      console.log(Recty);
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

// const r1 = new Rectangle(2, 3);
// console.log('Normal:');
// r1.print();

// console.log('Double:');
// r1.double();
// r1.print();

// console.log('Rotate:');
// r1.rotate();
// r1.print();

module.exports = Rectangle;
