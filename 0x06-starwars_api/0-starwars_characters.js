#!/usr/bin/node

const request = require('request');
const movieId = Number(process.argv[2]);
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(movieUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const characters = JSON.parse(body).characters;
  const promises = characters.map((url) => makeRequest(url));
  Promise.all(promises).then(responses => {
    responses.forEach((res) => console.log(res));
  });
});

function makeRequest (url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error || response.statusCode !== 200) {
        reject(error);
      }

      resolve(JSON.parse(body).name);
    });
  });
}
