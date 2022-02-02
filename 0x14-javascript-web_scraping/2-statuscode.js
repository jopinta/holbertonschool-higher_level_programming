#!/usr/bin/node
const argv = process.argv;
const quest = require('request');
quest(argv[2], function (error, response) {
  if (error) throw error;
  console.log('code:', response && response.statusCode);
});
