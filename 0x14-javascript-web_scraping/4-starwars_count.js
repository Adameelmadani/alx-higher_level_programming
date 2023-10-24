#!/usr/bin/node
const request = require('request');
const URL = process.argv[2];
const URL_CHAR = 'https://swapi-api.alx-tools.com/api/people/18/';

request(URL, function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body).results;
    let c = 0;
    for (const result of results) {
      if (result.characters.includes(URL_CHAR)) {
        c += 1;
      }
    }
    console.log(c);
  }
});
