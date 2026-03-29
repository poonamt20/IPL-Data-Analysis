
import pandas as pd

# Load data
matches = pd.read_csv('data/matches.csv')
deliveries = pd.read_csv('data/deliveries.csv')

# # Check data
# print("MATCHES DATA:")
# print(matches.head())

# print("\nDELIVERIES DATA:")
# print(deliveries.head())

# print(matches.columns)

import matplotlib.pyplot as plt

# # Use correct column name (change if needed)
# wins = matches['match_winner'].value_counts()
# wins.name = "Wins"
# print(wins)

# plt.figure(figsize=(10,5))
# wins.plot(kind='bar')

# plt.title("Most Winning Teams in IPL")
# plt.xlabel("Teams")
# plt.ylabel("Number of Wins")

# plt.xticks(rotation=45)
# plt.show()

# print(deliveries.columns)

# # Top batsmen (based on your dataset)
# top_batsmen = deliveries.groupby('striker')['runs_of_bat'].sum().sort_values(ascending=False).head(10)

# print("\nTop 10 Batsmen:")
# print(top_batsmen)

# plt.figure(figsize=(10,5))
# top_batsmen.plot(kind='bar')

# plt.title("Top 10 Batsmen in IPL")
# plt.xlabel("Players")
# plt.ylabel("Total Runs")

# plt.xticks(rotation=45)
# plt.show()
# # Filter valid wickets (exclude extras like run out)
# wickets = deliveries[deliveries['wicket_type'].notnull()]

# # Remove unwanted types
# wickets = wickets[~wickets['wicket_type'].isin(['run out', 'retired hurt', 'obstructing the field'])]
# top_bowlers = wickets['bowler'].value_counts().head(10)

# print("\nTop 10 Bowlers:")
# print(top_bowlers)
# plt.figure(figsize=(10,5))
# top_bowlers.plot(kind='bar')

# plt.title("Top 10 Bowlers in IPL")
# plt.xlabel("Bowlers")
# plt.ylabel("Wickets")

# plt.xticks(rotation=45)
# plt.show()
# runs = deliveries.groupby('striker')['runs_of_bat'].sum()
# balls = deliveries.groupby('striker').size()
# strike_rate = (runs / balls) * 100
# valid_players = balls[balls >= 100].index
# strike_rate = strike_rate[valid_players]
# top_sr = strike_rate.sort_values(ascending=False).head(10)

# print("\nTop 10 Strike Rate Players:")
# print(top_sr)
# plt.figure(figsize=(10,5))
# top_sr.plot(kind='bar')

# plt.title("Top 10 Strike Rate Players")
# plt.xlabel("Players")
# plt.ylabel("Strike Rate")

# plt.xticks(rotation=45)
# plt.show()
# Toss impact
toss_win_match_win = matches[matches['toss_winner'] == matches['match_winner']]

toss_counts = [
    len(toss_win_match_win),
    len(matches) - len(toss_win_match_win)
]

labels = ['Won Toss & Match', 'Won Toss but Lost Match']

plt.figure(figsize=(6,6))
plt.pie(toss_counts, labels=labels, autopct='%1.1f%%')

plt.title("Impact of Toss on Match Outcome")
plt.show()
# Matches per venue
venue_counts = matches['venue'].value_counts().head(10)

plt.figure(figsize=(12,6))
venue_counts.plot(kind='bar')

plt.title("Top 10 Venues by Number of Matches")
plt.xlabel("Venue")
plt.ylabel("Matches")

plt.xticks(rotation=45)
plt.show()