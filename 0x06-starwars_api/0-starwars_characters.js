#!/usr/bin/node

// script that prints all characters of a Star Wars movie
// Display one character name per line in the same order as the “characters” list in the /films/ endpoint

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);

  function getCharacters (idx) {
    if (idx === data.characters.length) {
      return;
    }
    const charUrl = data.characters[idx];
    request.get(charUrl, (error, response, body2) => {
      if (error) {
        console.error(error);
      } else {
        const characters = JSON.parse(body2);
        console.log(characters.name);
      }
      getCharacters(idx + 1);
    });
  }
  getCharacters(0);
});
