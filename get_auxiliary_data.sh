# Downloads data needed for data augmentation and training on auxiliary data.

# OSV5M download lol!
python downloader.py
python extractor.py

# Driving Side of the Road
python data/driving_side/driving_side.py

# Political boundaries
wget -O data/geocells/admin0.geojson https://github.com/wmgeolab/geoBoundaries/raw/refs/heads/main/releaseData/CGAZ/geoBoundariesCGAZ_ADM0.geojson
wget -O data/geocells/admin1.geojson https://github.com/wmgeolab/geoBoundaries/raw/refs/heads/main/releaseData/CGAZ/geoBoundariesCGAZ_ADM1.geojson
wget -O data/geocells/admin2.geojson https://github.com/wmgeolab/geoBoundaries/raw/refs/heads/main/releaseData/CGAZ/geoBoundariesCGAZ_ADM2.geojson

# GADM Country Area Data
curl --create-dirs -O --output-dir data/gadm https://geodata.ucdavis.edu/gadm/gadm4.1/gadm_410-levels.zip
cd data/gadm
unzip gadm_410-levels.zip
cd ../..

# GHSL Population Density Data
curl --create-dirs -O --output-dir data/pop_density https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/GHSL/GHS_POP_GLOBE_R2022A/GHS_POP_E2020_GLOBE_R2022A_54009_1000/V1-0/GHS_POP_E2020_GLOBE_R2022A_54009_1000_V1_0.zip
cd data/pop_density
unzip GHS_POP_E2020_GLOBE_R2022A_54009_1000_V1_0.zip
cd ../..

# Old Koppen-Geiger Climate Zone Data, now handled by the kgcpy package!
# curl --create-dirs -O --output-dir data/koppen_geiger https://s3-eu-west-1.amazonaws.com/pfigshare-u-files/12407516/Beck_KG_V1.zip
# cd data/koppen_geiger
# unzip Beck_KG_V1.zip
# cd ../..