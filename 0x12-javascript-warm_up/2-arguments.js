#!/usr/bin/node
// process command line arguments

const arg1 = process.argv[2];
const arg2 = process.argv[3];
if (arg2) {
  console.log('Arguments found');
} else if (arg1) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
