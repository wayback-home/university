const fs = require('fs');

fs.writeFile('/Users/choeyeongseo/Documents/ubuntu/nodejs/mobile/source/ch3/3.6/writeme.txt', '글이 입력됩니다', (err) => {
  if (err) {
    throw err;
  }
  fs.readFile('/Users/choeyeongseo/Documents/ubuntu/nodejs/mobile/source/ch3/3.6/writeme.txt', (err, data) => {
    if (err) {
      throw err;
    }
    console.log(data.toString());
  });
});
