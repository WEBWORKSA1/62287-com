#!/usr/bin/env python3
"""Weekly auto-refresh: rebuild pages (dates, sitemap lastmod, search index) and stamp status."""
import subprocess, sys, os
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
subprocess.check_call([sys.executable, "build.py"])
