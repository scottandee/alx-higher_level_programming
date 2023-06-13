#!/usr/bin/node
import { argv } from 'node:process';

if (argv.length === 2) {
  console.log('No arguents');
} else {
  console.log(argv[2]);
}
