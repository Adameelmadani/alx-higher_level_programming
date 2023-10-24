#!/usr/bin/node
const fs = require('fs');
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (!error) {
    const res = body;
    fs.writeFile(process.argv[3], res, (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
