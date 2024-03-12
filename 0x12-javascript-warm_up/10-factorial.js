#!/usr/bin/node

const arg = process.argv[2];
const number = parseInt(arg);

if (isNaN(number)) {
  console.log(1);
} else {
  let factorial = 1;
  for (let i = 2; i <= number; i++) {
    factorial *= i;
  }
  console.log(factorial);
}
