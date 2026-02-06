# CLI-based Card Game
A Python-based CLI game that includes an authentication system, local data persistence, and leaderboard sorting
###
Key Features:

User registration that validates unique usernames in a text file

Password strength validation that uses Regular Expressions to enforce policy (Min 6 chars, 1 uppercase, 1 digit, 1 special char)

Symmetric Encryption that implements a Rotational Cipher on user passwords before storage

###
Game Logic:

Color Hierarchy:

| Winner | Loser |
| :--- | :--- |
| Red | Black |
| Black | Yellow |
| Yellow | Red |

If colours match, the higher number wins


###
Data Persistence:

Stores user credentials in "UserData.txt"

Serializes game results into "ResultLogs.txt

###
Prerequisites:

Python version 3

###
How to play:

1. Sign up: create an account for both players

2. Login: Both player enter valid credentials in the CLI

3. The deck contains 30 cards, players draw cards in turns, the winning player takes both cards and the player with the most cards at the end of the deck wins
