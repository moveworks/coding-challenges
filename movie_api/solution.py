from fastapi import FastAPI

import requests
import json

app = FastAPI()

def get_all_movies():
    url = "https://us-central1-creator-studio-demo.cloudfunctions.net/movies"

    payload = {}
    headers = {
    'Authorization': 'Bearer ANY_VALUE'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response.json()

def get_movie_details(movie_id: str):
    url = "https://us-central1-creator-studio-demo.cloudfunctions.net/movieDetails"

    payload = json.dumps({
    "movie_id": movie_id
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ANY_VALUE'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()

def convert_minutes_to_hours_and_minutes(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    
    if hours == 0:
        return f"{remaining_minutes}min"
    elif remaining_minutes == 0:
        return f"{hours}h"
    else:
        return f"{hours}h {remaining_minutes}min"


@app.get("/api/movie-recommendations")
async def recommendations(genre: str, limit: int):
    movies = get_all_movies()['movies']
    genre_movies = list(filter(lambda x: x['genre'].lower() == genre.lower(), movies))
    
    movie_details = list(map(lambda x: get_movie_details(x['id']), genre_movies))
    total_run_time = sum(map(lambda x: x['run_time_minutes'], movie_details))
    average_rating = sum(map(lambda x: x['rating'], movie_details)) / len(movie_details)

    movie_response = list(map(lambda x: {
        "title": x['title'],
        'genre': x['genre'].lower(),
        'rating': round(x['rating'], 1),
        'relative_rating': round(x['rating'] - average_rating, 1),
        'run_time': convert_minutes_to_hours_and_minutes(x['run_time_minutes'])

    }, movie_details))



    return {"movies": movie_response, "metrics": {"total_run_time_minutes": total_run_time, "average_rating": average_rating}}
