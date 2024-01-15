#!/usr/bin/node
exports.esrever = function (list) {
  const newArri = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    newArri[j] = list[i];
    j++;
  }
  return newArri;
};
