#!/usr/bin/node
const request = require('request');
const filePath = 'https://swapi-api.alx-tools.com/api/films';
const id = process.argv[2];
request(`${filePath}/${id}/`, (error, response, body) => {
  if (!error) {
    console.log(JSON.parse(body).title);
  }
});
