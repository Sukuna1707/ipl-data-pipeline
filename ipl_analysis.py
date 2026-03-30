import pandas as pd
import sqlite3

# Read CSV
df = pd.read_csv('matches.csv')

# Create SQLite database
conn = sqlite3.connect('ipl_database.db')

# Load dataframe into database
df.to_sql('matches', conn, if_exists='replace', index=False)

print("Database created successfully")
print(f"Total rows loaded: {len(df)}")

# Query 1 - Most successful teams
query1 = """
SELECT winner, 
       COUNT(*) as total_wins
FROM matches
WHERE winner != ''
GROUP BY winner
ORDER BY total_wins DESC
LIMIT 5
"""

# Query 2 - Toss advantage analysis
query2 = """
SELECT toss_decision,
       COUNT(*) as total,
       SUM(CASE WHEN toss_winner = winner THEN 1 ELSE 0 END) as won_after_toss,
       ROUND(SUM(CASE WHEN toss_winner = winner THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) as win_percentage
FROM matches
GROUP BY toss_decision
"""

# Query 3 - Season wise matches and unique teams
query3 = """
SELECT Season,
       COUNT(*) as total_matches,
       COUNT(DISTINCT team1) as unique_teams
FROM matches
GROUP BY Season
ORDER BY Season
"""

# Run queries and print
print("\n--- Top 5 Teams ---")
print(pd.read_sql_query(query1, conn))

print("\n--- Toss Advantage Analysis ---")
print(pd.read_sql_query(query2, conn))

print("\n--- Season Summary ---")
print(pd.read_sql_query(query3, conn))

# Save results to JSON
pd.read_sql_query(query1, conn).to_json('top_teams.json', orient='records', indent=2)
pd.read_sql_query(query2, conn).to_json('toss_analysis.json', orient='records', indent=2)

print("\nResults saved to JSON files")
conn.close()