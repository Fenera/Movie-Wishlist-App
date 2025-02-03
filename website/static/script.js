api_key = API_KEY

const apiURL = `https://api.themoviedb.org/3/trending/movie/week?api_key=${api_key}`;

const moviesContainer = document.getElementById("movies");
const moreInfoContainer = document.getElementById("moreInfo");

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
    const { title, backdrop_path, vote_average, genre_ids} = media; 
    createInfoPage(media);

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

    // add to wishlist button
    const wishlist = document.createElement("button");
    wishlist.classList.add("wishlist_button");
    wishlist.textContent = "Add to wishlist";

    // learn more button
    const learnMore = document.createElement("button");
    learnMore.classList.add("learnMore_button");
    learnMore.textContent = "Learn More";


    // monitor clicks
    wishlist.addEventListener('click', () => {
        if(wishlist.textContent == "Add to wishlist"){
            wishlist.textContent = "Added!";
            
        }
        else{
            wishlist.textContent="Add to wishlist";
        }
    });

    //create function for MoreInfo
    function createInfoPage(media){
        //Add something
    }


    // create img element
    const img = document.createElement("img");
    // reason for two sizes is to avoid "img size not supported" error(https://www.themoviedb.org/talk/5a6986550e0a260d6400d6c0)
    img.src = backdrop_path 
    ? `https://image.tmdb.org/t/p/original/${backdrop_path}` // higher quality image
    : "https://via.placeholder.com/w780?text=No+Image"; // fallback to this size if other doesn't work
    img.classList.add("movie_img_rounded");


        // genre

    
    const genreType = document.createElement("div");
    genreType.classList.add("genre_type");

    // mapping genre ids to genres(https://www.themoviedb.org/talk/5daf6eb0ae36680011d7e6ee)
    const genreMap = {
        28: "Action",
        12: "Adventure",
        16: "Animation",
        35: "Comedy",
        80: "Crime",
        99: "Documentary",
        18: "Drama",
        10751: "Family",
        14: "Fantasy",
        36: "History",
        27: "Horror",
        10402: "Music",
        9648: "Mystery",
        10749: "Romance",
        878: "Science Fiction",
        10770: "TV Movie",
        53: "Thriller",
        10752: "War",
        37: "Western"
        };

    // convert the genre id to a readable genre(i.e 36 -> history)
    // array of genres(can be multiple)
    const genreNames = genre_ids.map(id => genreMap[id]).filter(Boolean); // .filter(Boolean) filters out null, undefined false.. genres
    // limit # of genres to 2 on movie card
    const displayGenre = genreNames.length > 2 ? genreNames.splice(0, 2) : genreNames;

    if(displayGenre.length > 0){
        genreType.textContent = displayGenre.join(", ");
    }
    else{
        genreType.textContent = "No genre";
    }

    // append to parent div
    movieInfo.appendChild(titleDiv);
    movieInfo.appendChild(ratingDiv);
    movieInfo.appendChild(wishlist);    
    
    movieCard.appendChild(genreType);
    movieCard.appendChild(img);
    movieCard.appendChild(movieInfo);
    movieCard.appendChild(learnMore);
    movieCard.appendChild(genreType);

    return movieCard;
}

fetchMovies();