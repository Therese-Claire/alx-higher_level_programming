#!/usr/bin/node
const arg = process.argv.slice(2);
const parsedNum = parseInt(arg[0]);

if (isNaN(parsedNum)) {
  console.log('Not a number');
} else {
  console.log('My number: ', parsedNum);
}
