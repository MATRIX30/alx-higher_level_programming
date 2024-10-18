#!/usr/bin/node
// script that prints first argument passed to it

const { argv } = require('node:process');
if (argv[2]) {
  console.log(argv[2]);
} else {
  console.log('No argument');
}
