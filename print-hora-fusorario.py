#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
from datetime import datetime, timedelta 

# Monta o horario brasileiro puxando o horario UTC e subtraindo 3 horas
brazilian_time = (datetime.utcnow() + timedelta(hours=-3)).strftime('%d/%m/%y %H:%M')

print(brazilian_time)

time.sleep(30)