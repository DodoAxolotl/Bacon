import json
import math
import argparse


def calculate_bacon_distance(db: dict, name: str) -> float:
    if "Kevin Bacon" not in db["actors"]:
        raise ValueError("Actor Kevin Bacon does not exist in our database")
    if name not in db["actors"]:
        raise ValueError(f"The specified actor does not exist in our database")
    distance = 0
    seen_movies = set()
    seen_actors = set(["Kevin Bacon"])
    current_movies = set()
    current_actors = set(["Kevin Bacon"])
    while name not in current_actors:
        if len(current_actors) == 0:
            return math.inf
        current_movies = set(
            [
                movie
                for actor in current_actors
                for movie in db["actors"][actor]
                if movie not in seen_movies
            ]
        )
        current_actors = set(
            [
                actor
                for movie in current_movies
                for actor in db["movies"][movie]
                if actor not in seen_actors
            ]
        )
        seen_movies.update(current_movies)
        seen_actors.update(current_actors)
        distance += 1
    return distance


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="bacon_distance")
    parser.add_argument("actor_name")
    args = parser.parse_args()
    with open("db.json") as file:
        db = json.load(file)
    print(calculate_bacon_distance(db, args.actor_name))
