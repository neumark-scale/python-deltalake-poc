#! /usr/bin/env bash
curl -o nz_census.zip 'https://www3.stats.govt.nz/2018census/Age-sex-by-ethnic-group-grouped-total-responses-census-usually-resident-population-counts-2006-2013-2018-Censuses-RC-TA-SA2-DHB.zip'
unzip nz_census.zip
rm nz_census.zip
