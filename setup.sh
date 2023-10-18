#! /usr/bin/env bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
curl -o nz_census.csv 'https://www3.stats.govt.nz/2018census/Age-sex-by-ethnic-group-grouped-total-responses-census-usually-resident-population-counts-2006-2013-2018-Censuses-RC-TA-SA2-DHB.zip'
