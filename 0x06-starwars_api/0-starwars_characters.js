#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  // Fetch character names in the same order using recursion
  const printCharacter = (index) => {
    if (index >= characters.length) return;
    request(characters[index], (err, res, charBody) => {
      if (!err) {
        const character = JSON.parse(charBody);
        console.log(character.name);
        printCharacter(index + 1);
      } else {
        console.error(err);
      }
    });
  };

  printCharacter(0);
});
