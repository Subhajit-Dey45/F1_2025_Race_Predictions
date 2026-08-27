print("Script is starting...")

import fastf1
import logging
import os

# Reduce terminal noise
logging.getLogger('fastf1').setLevel(logging.WARNING)

# 1. Setup cache for 2026
cache_folder = 'fastf1_2026_cache'
os.makedirs(cache_folder, exist_ok=True)
fastf1.Cache.enable_cache(cache_folder)

# 2. Fetch the 2026 season schedule
schedule = fastf1.get_event_schedule(2026)

print("Starting to cache the 2026 F1 Season (Skipping Pre-Season)...")

# 3. Loop through all events
for _, event in schedule.iterrows():
    
    # --- SKIP PRE-SEASON TESTING HERE ---
    if event['EventFormat'] == 'testing' or event['RoundNumber'] == 0:
        print(f"\n--- Skipping: {event['EventName']} (Pre-season testing) ---")
        continue
        
    print(f"\n--- Fetching: {event['EventName']} ---")
    
    # Fetch all sessions for the race weekend (Sessions 1 to 5)
    for session_num in range(1, 6):
        try:
            session = fastf1.get_session(2026, event['RoundNumber'], session_num)
            session.load(laps=True, telemetry=True, weather=True, messages=True)
            print(f"  [✓] Cached: {session.name}")
        except Exception as e:
            print(f"  [x] Skipped Session {session_num} (May not exist/not run yet)")

print("\n2026 caching complete!")