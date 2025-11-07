```markdown
# Assignment #4: Monitoring System with Prometheus & Grafana

**Student:** [Your Name]  
**Date:** November 2025  
**GitHub Repo:** https://github.com/your_username/your_repo_name  

---

## Project Overview

This project implements a full monitoring stack using:
- **PostgreSQL** as the database with hospital dataset
- **Prometheus** for metrics collection
- **Grafana** for visualization
- **Exporters**: PostgreSQL, Node, Custom (OpenWeather API)

All requirements from the assignment are met:
- 3 dashboards (DB, Node, Custom)
- 10+ PromQL queries per dashboard
- Global variables, alerts, real-time updates
- Load simulation
- Everything exported and pushed to GitHub

---

## Structure

```
.
├── docker-compose.yml          # All services (exporters + Prometheus + Grafana)
├── prometheus.yml              # Scrape configs
├── custom_exporter.py          # Custom weather exporter (10 metrics)
├── db-dashboard.json           # Dashboard 1: PostgreSQL Exporter
├── node-dashboard.json         # Dashboard 2: Node Exporter
├── custom-weather-dashboard.json # Dashboard 3: Custom Exporter
└── README.md                   # This file
```

---

## Quick Start

```bash
# 1. Clone repo
git clone https://github.com/your_username/your_repo_name.git
cd your_repo_name

# 2. Start everything
docker compose up -d

# 3. Run custom exporter (if not in Docker)
python3 custom_exporter.py

# 4. Open:
#    Prometheus: http://localhost:9090
#    Grafana:    http://localhost:3000 (admin/admin)
```

---

## Dashboards

### 1. DB Exporter - Hospital (30 points)
- 10 PromQL queries (QPS, connections, size, cache hit, etc.)
- Variable: `$db` (hospital)
- Alert: `DB Down`
- 4 visualization types

### 2. Node Exporter - System (25 points)
- CPU Heatmap, Load, RAM %, Disk I/O, Network
- Variable: `$instance`
- Alert: `High CPU Load > 80%`
- Load test with `stress --cpu 4`

### 3. Custom Exporter - Weather Moscow (45 points)
- 10 metrics from OpenWeatherMap API
- Update every 20 seconds
- 10 PromQL with math (pressure mmHg, wind km/h, day length, comfort index)
- Variable: `city=Moscow`
- Alert: `Heat > 30°C`

---

## Verification Commands

```bash
# Containers
docker ps

# Targets UP
curl http://localhost:9090/targets

# Custom metrics
curl http://localhost:8000/metrics

# Load generation (for Node Exporter)
stress --cpu 4 --timeout 300
```

---

## Defense Checklist

- [x] All containers UP
- [x] Targets: postgres, node, custom_weather → UP
- [x] 30 PromQL queries tested in Prometheus
- [x] 3 dashboards with variables & alerts
- [x] Real-time updates
- [x] Load simulation shown
- [x] All JSON exported
- [x] GitHub repo complete



Готово! Теперь ваш репозиторий выглядит профессионально и полностью соответствует требованиям задания.  

**Удачи на защите — вы сделали отличный проект!** 🚀
