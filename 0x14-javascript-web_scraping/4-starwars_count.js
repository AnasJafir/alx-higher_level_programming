#!/usr/bin/node
const request = require('request');

// API URL for Star Wars films
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';

// Function to count the number of movies where Wedge Antilles is present
function countMoviesWithWedge (callback) {
  request(apiUrl, function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const films = JSON.parse(body).results;
      let wedgeMoviesCount = 0;
      films.forEach(film => {
        const characters = film.characters;
        if (characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
          wedgeMoviesCount++;
        }
      });
      callback(null, wedgeMoviesCount);
    } else {
      callback(error || 'Failed to fetch data from API', null);
    }
  });
}

// Call the function to count movies with Wedge Antilles
countMoviesWithWedge(function (error, count) {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log(count);
  }
});
