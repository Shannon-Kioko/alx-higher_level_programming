#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const charId = 18;
const nbApp = [];
const charUrl = 'https://swapi-api.alx-tools.com/api/people';
request(url, (error, response, body) => {
  if (!error) {
    const jsonChar = JSON.parse(body).results;
    const characters = jsonChar.filter(x => x.characters.includes(`${charUrl}/18/`));
    console.log(characters.length);
  }
});
