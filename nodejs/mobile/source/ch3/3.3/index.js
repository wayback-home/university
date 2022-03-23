const { odd, even } = require('./var');
const {checkOddOrEven, checkXThree} = require('./func');
const checkThree = require('./check3');

function checkStringOddOrEven(str) {
  if (str.length % 2) { // 홀수면
    return odd;
  }
  return even;
}

console.log(checkOddOrEven(10));
console.log(checkStringOddOrEven('hello'));
console.log(checkXThree(12));
console.log(checkThree(10));
