#!/usr/bin/node
// Rectangle module

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
};
