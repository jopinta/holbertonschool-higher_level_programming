#!/usr/bin/node
const argv = process.argv;
const quest = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + argv;
quest(url, function (error, response, body) {
  if (error) throw error;
  console.log(JSON.parse(body).title);
});
