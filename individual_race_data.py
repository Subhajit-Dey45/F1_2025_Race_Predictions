print("Script is starting...")

import fastf1
import logging
import os

# Reduce terminal noise
logging.getLogger('fastf1').setLevel(logging.WARNING)

# 1. Setup cache
cache_folder = 'fastf1_2026_cache'
os.makedirs(cache_folder, exist_ok=True)
fastf1.Cache.enable_cache(cache_folder)

# 2. Define the target event and year
year = 2025
event_name = 'Race_name' #replace Race_name with actual race such as zandvoort or Dutch Grand Prix or Netherlands 

print(f"Starting to cache: {event_name} {year}...")

# 3. Loop through all 5 sessions of the race weekend (Practice, Quali, Race / Sprint)
for session_num in range(1, 6):
    try:
        # Load session using year, event name, and session index (1 to 5)
        session = fastf1.get_session(year, event_name, session_num)
        session.load(laps=True, telemetry=True, weather=True, messages=True)
        print(f"  [✓] Cached: {session.name}")
    except Exception as e:
        print(f"  [x] Skipped Session {session_num} - {e}")

print(f"\n{event_name} {year} caching complete!")
