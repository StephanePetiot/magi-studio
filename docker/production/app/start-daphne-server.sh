#!/bin/sh
daphne config.asgi:application --bind 0.0.0.0 -p 8001 --access-log -