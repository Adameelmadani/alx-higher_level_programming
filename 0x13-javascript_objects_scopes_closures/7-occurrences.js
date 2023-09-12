#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let n = 0;
  let i = 0;

  while (list[i]) {
    if (list[i] === searchElement) { n++; }
    i++;
  }
  return (n);
};
