#!/usr/bin/node
/**
 * function to reverse a speicific list
 * @param {list} list - list to be examined
 * @returns {number} - the reversed version of a list
 */
exports.esrever = function (list) {
    const newList = [];
    for (let i = list.length - 1; i >= 0; i--) {
      newList.push(list[i]);
    }
    return newList;
  };
