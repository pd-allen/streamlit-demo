import streamlit as st
import leafmap.foliumap as leafmap
import os.path
from os import path

def app():

    st.title("VectorData")

    out_dir = os.path.expanduser('~/Downloads')
    dem = os.path.join(out_dir, 'dem.tif')
    
    landsat = os.path.join(out_dir, 'landsat.tif')
    
    if not os.path.exists(dem):
        dem_url = 'https://drive.google.com/file/d/1vRkAWQYsLWCi6vcTMk8vLxoXMFbdMFn8/view?usp=sharing'
        leafmap.download_from_gdrive(dem_url, dem, out_dir, unzip=False)
    if not os.path.exists(landsat):
        landsat_url = 'https://github.com/giswqs/leafmap/raw/master/examples/data/cog.tif'
        leafmap.download_from_url(landsat_url, landsat, out_dir, unzip=False)   
    
    m = leafmap.Map()
    
    m.add_local_tile(dem, palette='viridis', layer_name="DEM")
    m.add_local_tile(landsat,  layer_name="Landsat")
    m.to_streamlit(height=900,width=1200)
    
app()
       