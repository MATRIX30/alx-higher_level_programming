#!/usr/bin/node

const fs = require('fs');

// Command-line arguments
const [, , inputFilePath1, inputFilePath2, outputFilePath] = process.argv;

// Read contents of the input files
const content1 = fs.readFileSync(inputFilePath1, 'utf8');
const content2 = fs.readFileSync(inputFilePath2, 'utf8');

// Concatenate contents
const concatenatedContent = content1 + content2;

// Write the concatenated content to the output file
fs.writeFileSync(outputFilePath, concatenatedContent);
