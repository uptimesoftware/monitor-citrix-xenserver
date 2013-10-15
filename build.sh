#!/bin/bash

# -- create the remote GitHub repository
REPONAME='zfs-zpool-status-monitor'

curl -u "uptime-grid" https://api.github.com/orgs/uptimesoftware/repos -d '{"name":"zfs-zpool-status-monitor", "team_id": 257186}'
git remote rm origin
git remote add origin https://uptime-grid@github.com/uptimesoftware/zfs-zpool-status-monitor.git
git push -u origin master

