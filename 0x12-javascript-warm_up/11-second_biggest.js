#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
} else {
  let max1 = Number.MIN_SAFE_INTEGER;
  let max2 = Number.MIN_SAFE_INTEGER;

  for (let i = 0; i < args.length; i++) {
    if (args[i] > max1) {
      max2 = max1;
      max1 = args[i];
    } else if (args[i] > max2 && args[i] !== max1) {
      max2 = args[i];
    }
  }

  console.log(max2);
}
