print("Script is starting...")

import fastf1
import logging
import os

# Reduce terminal noise
logging.getLogger('fastf1').setLevel(logging.WARNING)

# 1. Setup cache
cache_folder = 'fastf1_2025_cache'
os.makedirs(cache_folder, exist_ok=True)
fastf1.Cache.enable_cache(cache_folder)

# 2. Fetch the 2025 season schedule
schedule = fastf1.get_event_schedule(2025)

print("Starting to cache the 2025 F1 Season (Skipping Pre-Season)...")

# 3. Loop through all events
for _, event in schedule.iterrows():
    
    # --- SKIP PRE-SEASON TESTING HERE ---
    if event['EventFormat'] == 'testing' or event['RoundNumber'] == 0:
        print(f"\n--- Skipping: {event['EventName']} (Pre-season testing) ---")
        continue
        
    print(f"\n--- Fetching: {event['EventName']} ---")
    
    # Fetch all 5 sessions for the race weekend
    for session_num in range(1, 6):
        try:
            session = fastf1.get_session(2025, event['RoundNumber'], session_num)
            session.load(laps=True, telemetry=True, weather=True, messages=True)
            print(f"  [✓] Cached: {session.name}")
        except Exception as e:
            print(f"  [x] Skipped Session {session_num} (May not exist/cancelled)")

print("\n2025 caching complete!")