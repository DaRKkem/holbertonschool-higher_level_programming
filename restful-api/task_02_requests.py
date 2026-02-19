#!/usr/bin/python3
"""Task 02 - Consuming and processing data from an API using Python"""

import requests
import csv


API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch all posts from JSONPlaceholder and print their titles."""
    response = requests.get(API_URL)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetch all posts from JSONPlaceholder and save
       them into posts.csvwith columns: id, title, body."""
    response = requests.get(API_URL)

    if response.status_code == 200:
        posts = response.json()

        structured_data = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body"),
            }
            for post in posts
        ]

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(structured_data)
