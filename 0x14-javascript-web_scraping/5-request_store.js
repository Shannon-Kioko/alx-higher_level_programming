#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const path = process.argv[3];

request(url, (error, response, body) => {
  if (!error) {
    console.log(body);
    fs.writeFile(path, body, 'utf-8', err => {
      if (err) {
        console.log(err);
      } else {
        console.log('Saved');
      }
    });
  }
});
