# Movie API Coding Challenge

## The Challenge

### Objective

You are tasked with creating a Movie Recommendation API using [two publicly available REST APIs](https://developer.moveworks.com/creator-studio/demo-functions/). The new recommendation API will accept a movie genre that a user cares about and come up with possible movies to watch.

### Success Criteria

Your API should have the following request & response behavior.

```bash Example Request
curl --location --globoff '{{base_url}}/api/movie-recommendations?genre=Action&limit=5'
```

```json Example Response
{
 "metrics": {
  "total_run_time_minutes": 823
 } 
 "results": [
  {
   "title": "Transformers",
   "genre": "action",
   "rating": 3.8,
   "relative_rating": "-0.3"
   "release_year": 2023,
   "run_time": "2h 3min"
  },
  ...
 ]
}
```

### Implementation Instructions

👉 Ensure you handle possible errors and exceptions gracefully, such as handling invalid genre inputs, API errors, or empty responses.

1. Fetch a list of all popular movies using an API call
2. Filter the movies based on the genre (determined by the `genre` parameter – case insensitive)
3. For each movie, get additional details for the movie using another API call
4. Calculate the total run time of movies in the genre
5. Calculate the average rating of movies in the genre
6. For each movie in the genre, store the following details
    - **Title (`title`)** - The exact title of the movie as returned by the API
    - **Genre (`genre`)** - The genre of the movie (all lowercase)
    - **Rating (`rating`)** - The rating of the movie, rounded to 1 decimal point
    - **Relative Rating (`relative_rating`)** - `rating` minus the average rating of movies in the genre
    - **Runtime (run_time)** - The movie runtime in a human-friendly format (formatted as “Xh Ymin”) where X is the number of hours & Y is the number of minutes
7. Sort the movies based on relative rating (highest first), and trim to the first N records (determined by the `limit` parameter)
8. Return all the data following this format:

    ```json
    {
     "metrics": {
      "total_run_time_minutes": 823
     } 
     "results": [
      {
       "title": "Transformers",
       "genre": "action",
       "rating": 3.8,
       "relative_rating": "-0.3"
       "run_time": "2h 3min"
      },
      ...
     ]
    }
    ```

## Tools for building

**Pro-code?**

- [Node.JS + Express](https://expressjs.com/en/starter/hello-world.html)
- [Python + FastAPI](https://fastapi.tiangolo.com/tutorial/)
- [Python + Flask](https://flask.palletsprojects.com/en/2.3.x/quickstart/)

**Low-code?**

- Use an [enterprise automation tool](https://developer.moveworks.com/creator-studio/automation-tools) that you’re comfortable with

## Reference Materials

You can use the APIs hosted with our [Demo Functions](https://developer.moveworks.com/creator-studio/demo-functions/) to build your use case.

🎉 Good luck! Happy coding! 👩‍💻
