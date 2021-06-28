#!/bin/bash
ip=$(hostname -I | awk '{print $1}')
sed -i 's/{IP}/'$ip'/g' /app/sample.py
python /app/sample.py

