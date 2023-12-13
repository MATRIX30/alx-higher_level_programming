#!/usr/bin/node
/*
Your script must import list from the file 100-data.js
You must use a map. Tips
A new list must be created with each value equal to the value of the initial list, multipled by the index in the list
Print both the initial list and the new list
*/
const lists = require('./100-data').list;
console.log(lists);
const newList = lists.map((items, index) => items * index);
console.log(newList);
