#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (!error) {
    const JSON_RES = JSON.parse(body);
    const JSON_DICT = {};
    for (let i = 1; i <= 10; i++) {
      let c = 0;
      for (const task of JSON_RES) {
        if (task.userId === i) {
          if (task.completed === true) {
            c += 1;
          }
        }
      }
      const STR_ID = '' + i;
      JSON_DICT[STR_ID] = c;
    }
    console.log(JSON_DICT);
  }
});
