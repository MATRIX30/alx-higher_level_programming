#!/usr/bin/node
// Create an instance method called print()
// that prints the rectangle using the character X

module.exports = class Rectangle {
  // rectangle class

  constructor (w = -1, h = -1) {
    if ((w <= 0) || (h <= 0)) {
    // Do nothing
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write('X');
      }
      console.log('');
    }
  }
};
