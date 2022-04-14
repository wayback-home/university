const http = require('http');

http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
  res.write('<h1>Hello Node!</h1>');
  res.write('<h3>8080 Port</h3>');
  res.end('<p>Hello Server!</p>');
})
  .listen(8080, () => { // 서버 연결
    console.log('8080번 포트에서 서버 대기 중입니다!');
  });


http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
  res.write('<h1>Hello Node!</h1>');
  res.write('<h3>8081 Port</h3>');
  res.end('<p>Hello Server!</p>');
})
  .listen(8081, () => { // 서버 연결
    console.log('8081번 포트에서 서버 대기 중입니다!');
  });


http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
  res.write('<h1>Hello Node!</h1>');
  res.write('<h3>8082 Port</h3>');
  res.end('<p>Hello Server!</p>');
})
  .listen(8082, () => { // 서버 연결
    console.log('8082번 포트에서 서버 대기 중입니다!');
  });


http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
  res.write('<h1>Hello Node!</h1>');
  res.write('<h3>8083 Port</h3>');
  res.end('<p>Hello Server!</p>');
})
  .listen(8083, () => { // 서버 연결
    console.log('8083번 포트에서 서버 대기 중입니다!');
  });


http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
  res.write('<h1>Hello Node!</h1>');
  res.write('<h3>8084 Port</h3>');
  res.end('<p>Hello Server!</p>');
})
  .listen(8084, () => { // 서버 연결
    console.log('8084번 포트에서 서버 대기 중입니다!');
  });


http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
  res.write('<h1>Hello Node!</h1>');
  res.write('<h3>8085 Port</h3>');
  res.end('<p>Hello Server!</p>');
})
  .listen(8085, () => { // 서버 연결
    console.log('8085번 포트에서 서버 대기 중입니다!');
  });
