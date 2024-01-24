#!/usr/bin/node
const request = require('request')

const movieId = process.argv[2]
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`

request(url, (err, response, body) => {
    if(!err){
        const characters = JSON.parse(body).characters
        characters.forEach(x => {
            request(x, (err,response, body) => {
                if(err) console.log(err);
                const charaName = JSON.parse(body).name
                console.log(charaName);

            })
            
        });
    }
})