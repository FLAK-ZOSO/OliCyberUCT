#!/usr/bin/env python3
from __future__ import annotations
import requests
import typing


class User:
    def __init__(self, user_id: int):
        self.id = user_id

    def get_stats(self, debug: bool=False) -> None:
        self.stats = fetch_user_stats(self.id, debug)
        if self.stats["extended"]:
            self.nickname = self.stats["nickname"]
            self.name = self.stats["name"]
            self.surname = self.stats["surname"]
        else:
            self.nickname = self.stats["displayedName"]
        self.correct_submissions = self.stats["correctSubmissions"]
        self.score = self.stats["score"]

    def print_basic_stats(self, full: bool=False) -> None:
        if self.stats["extended"] and full:
            print(f"\x1b[31m{self.nickname}\x1b[0m (\x1b[33m{self.name}\x1b[0m \x1b[33m{self.surname}\x1b[0m)", end='')
        else:
            print(f"\x1b[31m{self.nickname}\x1b[0m", end='')
        print(f" with \x1b[32m{self.correct_submissions}\x1b[0m correct submissions has \x1b[32m{self.score}\x1b[0m points")

    def get_solves_(self, information: str="id") -> set[int | str | tuple[int, str]]:
        if information == "id":
            return {
                self.stats["solves"][i]["challengeId"]
                for i in range(len(self.stats["solves"]))
            }
        elif information == "title":
            return {
                self.stats["solves"][i]["challengeTitle"]
                for i in range(len(self.stats["solves"]))
            }
        elif information == "both":
            return {
                (self.stats["solves"][i]["challengeId"], self.stats["solves"][i]["challengeTitle"])
                for i in range(len(self.stats["solves"]))
            }

    def missing_challenges_from(self, other: User, information: str="id") -> set[int | str]:
        return other.get_solves_(information) - self.get_solves_(information)


def fetch_user_stats(user_id: int, debug: bool=False) -> dict:
    assert isinstance(user_id, int)
    headers = {
        "accept": "application/json",
        "authority": "training.olicyber.it",
        "accept-language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
        "authorization": "Token 2a499b3a-e3d8-479e-b8a9-b3de126bd098",
        "Referer": f"https://training.olicyber.it/player/{user_id}"
    }
    response = requests.get(
        f"https://training.olicyber.it/api/scoreboard/player/{user_id}",
        headers=headers
    )
    if debug:
        print(response.status_code)
        print(response.text)
        print(response.url)
    response_json: dict[str, typing.Any] = response.json()
    if response.status_code == 200:
        if "code" not in response_json.keys():
            return response_json
        if response_json["code"] == "INVALID_REQUEST":
            if response_json["message"] == "The player is not valid":
                raise ValueError(f"The player {user_id} doesn't exist")
            else:
                raise ValueError(f"Unknown error: {response_json['message']}")
        else:
            return response_json


def print_basic_user_stats(stats: dict[str, bool | str | int | dict | list]):
    if stats["extended"]:
        print(f"{stats['nickname']} ({stats['name']} {stats['surname']})")
    else:
        print(stats['displayedName'])
    print(f"With {stats['correctSubmissions']} correct submissions has {stats['score']} points")


if __name__ == "__main__":
    flak = User(6606)
    flak.get_stats()
    flak.print_basic_stats()
    sere = User(4244)
    sere.get_stats()
    sere.print_basic_stats()
    subtraction = flak.missing_challenges_from(sere)
    print(f"{flak.nickname} is missing {len(subtraction)} challenges from {sere.nickname}")
    subtraction = sere.missing_challenges_from(flak)
    print(f"{sere.nickname} is missing {len(subtraction)} challenges from {flak.nickname}")
    subtraction = flak.missing_challenges_from(sere, "title")
    print(f"The challenges {flak.nickname} is missing from {sere.nickname}: {subtraction}")