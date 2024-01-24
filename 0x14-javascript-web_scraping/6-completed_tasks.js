#!/usr/bin/node
const request = require('request')

const url = process.argv[2]
request(url, (err, response, body) => {
    const nbTasks = {}
    if (!err) {
        const taskers = JSON.parse(body)
        console.log(taskers);
        taskers.forEach(x => {
            if (x.completed) {
                if (!nbTasks[x.userId]) {
                    nbTasks[x.userId] = 0;
                }
                nbTasks[x.userId]++
            }
        });
    }
    console.log(nbTasks);
})