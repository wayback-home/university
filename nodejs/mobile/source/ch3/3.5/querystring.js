const url = require('url');
const querystring = require('querystring');

const parsedUrl = url.parse('https://www.acmicpc.net/problem/1000');
const query = querystring.parse(parsedUrl.query);
console.log('querystring.parse():', query);
console.log('querystring.stringify():', querystring.stringify(query));
