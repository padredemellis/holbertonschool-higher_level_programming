#!/usr/bin/node
const args = procces.argv.slice(2);

while (args) {
  if (args[0] === undefined) {
    console.log('No argument');
  } else {
    console.log(args[0]);
  }
}