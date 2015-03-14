#!/bin/sh

# Executed daily by an external cron job, will update the repository and the
# user-crontab.

git fetch && git reset --hard origin/master && crontab ./crontab
