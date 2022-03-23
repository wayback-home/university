const { odd, even } = require('./var');

function checkOddOrEven(num) {
  if (num % 2) { // 홀수면
    return odd;
  }
  return even;
}

function checkXThree(num) {
  if (num % 3 == 0){
    return "3의 배수입니다"
  }
  return "3의 배수가 아닙니다."
}

module.exports = {
  checkOddOrEven,
  checkXThree
};

