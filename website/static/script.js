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
    const { title, backdrop_path, vote_average } = media; 

    // new div element for the movie card
    const movieCard = document.createElement("div");

    // Add the class 'movie_item' to style the movie card
    movieCard.classList.add("movie_item");

    
    // title and rating container
    const movieInfo = document.createElement("div");
    movieInfo.classList.add("movie_info");

    // create title element
    const titleDiv = document.createElement("div");
    titleDiv.textContent = title || "Untitled";

    const ratingDiv = document.createElement("div");
    ratingDiv.textContent = `⭐ ${vote_average.toFixed(1)} / 10`;

    // add to wishlist 
    const wishlist = document.createElement("button");
    wishlist.classList.add("wishlist_button");
    wishlist.textContent = "Add to wishlist";

    // action listener
    wishlist.addEventListener('click', () => {
        if(wishlist.textContent == "Add to wishlist"){
            wishlist.textContent = "Added!"
            
        }
        else{
            wishlist.textContent="Add to wishlist";
        }
    });
    // create img element
    const img = document.createElement("img");
    // reason for two sizes is to avoid "img size not supported" error(https://www.themoviedb.org/talk/5a6986550e0a260d6400d6c0)
    img.src = backdrop_path 
    ? `https://image.tmdb.org/t/p/original/${backdrop_path}` // higher quality image
    : "https://via.placeholder.com/w780?text=No+Image"; // fallback to this size if other doesn't work
    img.classList.add("movie_img_rounded");

    // append to parent div

    movieInfo.appendChild(titleDiv);
    movieInfo.appendChild(ratingDiv);
    movieInfo.appendChild(wishlist);    
    

    movieCard.appendChild(img);
    movieCard.appendChild(movieInfo);

    return movieCard;
}

fetchMovies();