api_key = API_KEY

const apiURL = `https://api.themoviedb.org/3/trending/movie/week?api_key=${api_key}`;


const moviesContainer = document.getElementById("movies");

async function fetchMovies() {
    try {
        // fetch the data 
        const response = await fetch(apiURL);

        const data = await response.json();

        // for each movie (media) in the array, create and append a movie card
        data.results.forEach(media => {
            const movieCard = createMovieCard(media);  
            moviesContainer.appendChild(movieCard);  
        });

    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

function createMovieCard(media) {
    const { title, name, backdrop_path } = media; // destructure

    // new div element for the movie card
    const movieCard = document.createElement("div");

    // Add the class 'movie_item' to style the movie card
    movieCard.classList.add("movie_item");

    movieCard.innerHTML = `
        <img src="https://image.tmdb.org/t/p/w500/${backdrop_path}" class="movie_img_rounded">
        <div class="title">${title || name}</div>
    `;

    return movieCard;
}

fetchMovies();