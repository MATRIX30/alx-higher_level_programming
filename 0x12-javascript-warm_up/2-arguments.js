#!/usr/bin/node
// print message depending on # of arguments
const { argv } = require('node:process');
const argCount = argv.length - 2;
if (argCount === 0) {
  console.log('No argument');
} else if (argCount === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
