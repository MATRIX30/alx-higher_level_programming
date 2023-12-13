#!/usr/bin/node
/*
The first argument is the file path of the first source file
The second argument is the file path of the second source file
The third argument is the file path of the destination
*/
const files = require('files');
const file1 = files.readFileSync(process.argv[2], 'utf8');
const file2 = files.readFileSync(process.argv[3], 'utf8');
files.writeFileSync(process.argv[4], file1 + file2);
