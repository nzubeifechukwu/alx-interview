#!/usr/bin/node
/**
 * Print all characters of a Star Wars movie, where the episode number matches
 * a given integer, passed as the first argument.
 */
const request = require('request');
const process = require('process');

const getResponse = (url) => {
  // const response = await fetch(url);
  // const data = await response.json();
  // return data;
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      }
      resolve(JSON.parse(body));
    });
  });
};

const fetchCharacters = async (id) => {
  try {
    const movie = await getResponse(`https://swapi-api.alx-tools.com/api/films/${id}`);
    const characterUrls = await movie.characters;

    for (const url of characterUrls) {
      const character = await getResponse(url);
      const name = await character.name;
      console.log(name);
    }
  } catch (error) {

  }
};

fetchCharacters(process.argv[2]);
