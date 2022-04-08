const fs = require('fs');

const writeStream = fs.createWriteStream('./writeme2.txt');
writeStream.on('finish', () => {
  console.log('파일 쓰기 완료');
});

writeStream.write('이 글을 씁니다.\n');
writeStream.write('한 번 더 씁니다.\n');
writeStream.write('두 번 더 씁니다.\n');

for (let index = 0; index < 10; index++) {
  writeStream.write((index+1)+" 번 더 씁니다.\n");
  
}

writeStream.end();
