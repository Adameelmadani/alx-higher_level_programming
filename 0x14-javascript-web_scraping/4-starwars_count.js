#!/usr/bin/node
const request = require('request');
const URL = process.argv[2];

request(URL, function (error, response, body) {
  if (!error) {
    const results = JSON.parse(body).results;
    let c = 0;
    for (const result of results) {
      for (const MY_CHAR of result.characters) {
        if (MY_CHAR.includes(18)) {
          c += 1;
        }
      }
    }
    console.log(c);
  } else {
    console.error(error);
  }
});
