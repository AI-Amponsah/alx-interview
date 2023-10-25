#!/usr/bin/node

const request = require('request');
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

function fetchCharacterData (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (!error && response.statusCode === 200) {
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      }
    });
  });
}

function fetchAndPrintCharacterNames (movieUrl) {
  request(movieUrl, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const movieData = JSON.parse(body);
      const characterUrls = movieData.characters;

      const promises = characterUrls.map(fetchCharacterData);

      Promise.all(promises)
        .then(characterNames => {
          characterNames.forEach(name => console.log(name));
        });
    }
  });
}

fetchAndPrintCharacterNames(movieUrl);
