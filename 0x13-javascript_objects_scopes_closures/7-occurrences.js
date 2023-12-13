#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const filteredList = list.filter((currentElement) => currentElement === searchElement);
  return filteredList.length;
};
