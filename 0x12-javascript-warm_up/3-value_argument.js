#!/usr/bin/node
// prints  1st value passed to it
// else prints No argument

const arg = process.argv[2];
if (!arg) {
  console.log('No argument');
} else {
  console.log(arg);
}
