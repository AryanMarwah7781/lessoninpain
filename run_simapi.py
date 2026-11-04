"""Start the simulator API:  python -I run_simapi.py [--log tail|udp] [--port 47900]"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from simapi.server import main  # noqa: E402

main()
