#!/usr/bin/node
// process command line arguments
// const arg1 = process.argv[2]
// const arg2 = process.argv[3]

const arg_count = process.argv.length
if (arg_count >= 4) {
  console.log('Arguments found')
} else if (arg_count === 3) {
  console.log('Argument found')
} else {
  console.log('No argument')
}
