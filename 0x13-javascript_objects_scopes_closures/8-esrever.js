#!/usr/bin/node

exports.esrever = function (list) {
  const newlist = [];
  let i = list.length - 1;
  while (i !== -1) {
    newlist.push(list[i]);
    i--;
  }
  return (newlist);
};
