#!/usr/bin/env python3
import psutil


cpu_stats = psutil.cpu_percent(0.5)

print("CPU usage",cpu_stats,"%")
