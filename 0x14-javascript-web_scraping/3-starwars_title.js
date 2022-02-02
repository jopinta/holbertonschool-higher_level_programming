#!/usr/bin/node
const argv = process.argv;
const val = argv[2];
const quest = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + val;
quest(url, function (error, response, body) {
  if (error) throw error;
  console.log(JSON.parse(body).title);
});
