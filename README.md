# Real-Time Process Monitoring Dashboard

This is our CSE316 project at Lovely Professional University. It’s a tool that tracks your computer’s CPU and memory usage live, shows graphs, and warns you if they get too high. We made it in Python and split it into three parts.

## What It Does
- Checks CPU and memory every second for a minute.
- Draws live graphs (CPU in blue, memory in red).
- Alerts if CPU > 80% or memory > 80%, plus shows averages.

## How to Run It
1. Get Python 3 (from python.org if you don’t have it).
2. Install stuff:

3. Download the files from this repo.
4. Run:


## The Parts
- **Data Collection (`data_collection.py`):** Grabs CPU and memory numbers.
- **Visualization (`visualization.py`):** Makes the graphs you see.
- **Monitoring & Alerts (`monitoring_alerts.py`):** My part—warns if stuff’s high and calculates averages.

`main.py` runs it all together.

## Who Did It
- **Member 1:** Data Collection.
- **Member 2:** Visualization.
- **Me:** Monitoring & Alerts

## What We Used
- **Python** and these libraries:
- `psutil` for system stats.
- `matplotlib` for graphs.
- `numpy` (just in case).
- `IPython.display` to update graphs.

## Notes
- Runs 60 seconds, alerts at 80% (I tweaked it from 85%).
- Stop it early with Ctrl+C.

## Future Ideas
- Show running processes.
- Send alerts as emails.

Check the commits to see our work!
