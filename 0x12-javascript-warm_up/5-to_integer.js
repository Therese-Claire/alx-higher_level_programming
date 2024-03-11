#!/usr/bin/node
const arg = process.argv[2];
const parsedNum = parseInt(arg);

if (isNaN(parsedNum)) {
  console.log('Not a number');
} else {
  console.log('My number: ', parsedNum);
}
