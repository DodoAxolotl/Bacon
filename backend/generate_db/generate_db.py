import csv
import json
from pathlib import Path
from typing import Dict, Tuple, List


def generate_db() -> None:
    movie_names = get_all_movies()
    movies, actors = get_all_roles(movie_names)
    get_all_actors(movies, actors)
    db = {"movies": movies, "actors": actors}
    with open(Path(__file__).parent.parent / "db.json", "w") as file:
        json.dump(db, file)


def get_all_actors(movies: Dict[str, List[str]], actors: Dict[str, List[str]]) -> None:
    with open(Path(__file__).parent / "name.basics.tsv", newline="", encoding="utf-8") as file:
        content = csv.DictReader(file, delimiter="\t")
        for row in content:
            if row["nconst"] in actors:
                actor, name = row["nconst"], row["primaryName"]
                actors[name] = actors.pop(actor)
                for movie in actors[name]:
                    movies[movie].remove(actor)
                    movies[movie].append(name)


def get_all_roles(
    movie_names: Dict[str, str],
) -> Tuple[Dict[str, List[str]], Dict[str, List[str]]]:
    movies = {}
    actors = {}
    with open(Path(__file__).parent / "title.principals.tsv", newline="", encoding="utf-8") as file:
        content = csv.DictReader(file, delimiter="\t")
        for row in content:
            if row["tconst"] in movie_names and row["characters"] != "\\\\N":
                movie, actor = movie_names[row["tconst"]], row["nconst"]
                movies.setdefault(movie, [])
                movies[movie].append(actor)
                actors.setdefault(actor, [])
                actors[actor].append(movie)
    return movies, actors


def get_all_movies() -> Dict[str, str]:
    movie_names = {}
    with open(Path(__file__).parent / "title.basics.tsv", newline="", encoding="utf-8") as file:
        content = csv.DictReader(file, delimiter="\t")
        for row in content:
            if row["titleType"] == "movie" and row["startYear"] == "1978":
                movie_names[row["tconst"]] = row["primaryTitle"]
    return movie_names


if __name__ == "__main__":
    generate_db()
