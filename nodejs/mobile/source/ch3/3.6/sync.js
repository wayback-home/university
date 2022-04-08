const fs = require('fs');


console.log('시작');
let data = fs.readFileSync('./readme2.txt');

console.time();

for (let index = 0; index < 100000; index++) {
    console.log(index+"번",data.toString());
    data = fs.readFileSync('./readme2.txt');
    
}

console.log('끝');
console.timeEnd();