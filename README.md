# No Man's Sky Galactic Map
* **Author**: Derek Borders, [github: Derek-Borders](https://github.com/Derek-Borders)  
* **Major**: CSCI (BS), Data Science (Certificate)  
* **Year**: Fall 2022  

# Type of project  

Primary: image classification via neural network  
Secondary: web scraper, dataset creation/curation, Plotly-Dash web app

# Purpose (including intended audience)  
Use a neural-network based workflow to extract coordinates from screen shots to create interactive 3D maps (scatter plot, surface plot, heatmap) of personally expored and community-explored space in the starting galaxy of the game *No Man's Sky*. 

## Fulfilling a 'need' 
An interactive 3D map of the fictional galaxy 'Euclid', the starting galaxy in the game *No Man's Sky*. The game has a nice interface for exploring nearby systems as well as a thumbnail-sized image of the whole galaxy with a small 'you are here' marker. However, there is no easy way for players to see where they have been or where others have been at a glance. Additionally, the galaxy image seems like an art asset that does not reflect the overall shape and structure of the actual simulated galaxy.

## Learning Objectives    
- exposure to neural networks in a less canned way than with something like a Kaggle exercise  
- exposure to building dashboards with Plotly Dash  
- further refine data visualization skills, particularly for a dataset with strong spatial components  
- practice web scraping  
- practice building a usable dataset from scratch with 'real world' data  
- practice finding and utilizing libraries, modules, and APIs to achieve a complex goal  

## Target Audience & Scope  
To start with this is a tool for personal use. This could foreseeably be expanded into a public facing web application to allow other players to upload their own screenshots to visualize their own journeys. Additionally, this could potentially be connected to other existing community tools like the No Man's Sky Coordinate Exchange's database of submitted coordinates.



# Explanation of files

The files are a mess at this time.


* `dash/` - files needed for the dash app  
  * `assets/` - boilerplate directory for dash apps
    * `reset.css` - started as a standard `reset.css` file and was pared down to a background color reset. Not sure it's actually in use in this version of `app.py`  
  * `data/` - `.csv` files used by `app.py`  
    * `galaxy_center.csv` - values used to visualize the 'supermassive black hole' at the galaxy center.   
      - Variables: size, dist, opacity, color (all used to style markers in `app.py`)  
    * `my_star_systems.csv` - values extracted from my personal screenshots
      - Variables:    
        (index): unnamed column used for pandas dataframe index  
        address: hexadecimal address extracted from screenshot  
        body_index_h: hexadecimal. derived. symbol 0 of address, planet/moon number  
        sys_index_h: hexadecimal. derived. symbols 1-3, system number within region  
        region_y_h: hexadecimal. derived. symbols 4 & 5, 'y' position, or voxel distance from 'galactic plane' (x,z plane)  
        region_x_h: hexadecimal. derived. symbols 6-8, 'x' position, or voxel distance from 'galactic N/S plane' (y,z plane)  
        region_z_h: hexadecimal. derived. symbols 9-11, 'z' position, or voxel distance from 'galactic E/W plane' (x,y plane)  
        planet_index: decimal conversion of corresponding hex value above  
        sys_index: decimal conversion of corresponding hex value above  
        y: ones complement of decimal conversion of corresponding hex value above  
        x: ones complement of decimal conversion of corresponding hex value above  
        z: ones complement of decimal conversion of corresponding hex value above  
        k_ly_from_center: calculated euclidian distance from (0,0,0) multiplied by .4 to account for size (400 light years) of simulated region voxels (3d pixels)  
    * `reddit_star_systems.csv` - values extracted from my personal screenshots
      - ***Variables***:  
        :**(index)** unnamed column used for pandas dataframe index  
        **post_id**: primary key for posts in Reddit API  
        **author_id**: post author user id primary key in reddit api
        **flair_text**: post flair (topic/category)
        **subject**: derived, extracted from flair_text, the subject of the screenshot (ship, planet, frigate, freighter, fauna, base, multitool)
        **galaxy**: derived, extracted from flair_text, alway euclid for this set
        **update**: derived, extracted from flair_text, game version screenshot came from
        **url**: address of image. Also post address where post is not a gallery
        **address**: hexadecimal address extracted from screenshot  
        **body_index_h**: hexadecimal. derived. symbol 0 of address, planet/moon number  
        **sys_index_h**: hexadecimal. derived. symbols 1-3, system number within region  
        **region_y_h**: hexadecimal. derived. symbols 4 & 5, 'y' position, or voxel distance from 'galactic plane' (x,z plane)  
        **region_x_h**: hexadecimal. derived. symbols 6-8, 'x' position, or voxel distance from 'galactic N/S plane' (y,z plane)  
        **region_z_h**: hexadecimal. derived. symbols 9-11, 'z' position, or voxel distance from 'galactic E/W plane' (x,y plane)  
        **planet_index**: decimal conversion of corresponding hex value above  
        **sys_index**: decimal conversion of corresponding hex value above  
        **y**: ones complement of decimal conversion of corresponding hex value above  
        **x**: ones complement of decimal conversion of corresponding hex value above  
        **z**: ones complement of decimal conversion of corresponding hex value above  
        **k_ly_from_center**: calculated euclidian distance from (0,0,0) multiplied by .4 to account for size (400 light years) of simulated region voxels (3d pixels)
* `production_scripts/` - 'final product' notebooks, images, and source code. These are slightly less messy, more focused files used in the final version of the project at time of presentation  
* `test_scripts/` - early exploration notebooks, images, and source code. very messy files created and used while exploring the various tools and figuring out the workflow for the project overall  
* `poster/` - presentation poster and related files  
* `proposal/` - proposal presentation slides, partial draft document form proposal, related files  


# Completion status 

## Completed Milestones  
- Neural network trained.  
- Currently works on most 16:9 images with near 100% accuracy.  
- Web scraping and classification function worked (sort of) but was done extremely suboptimally. Not recommended for reuse without significant refactoring.  
- Dash app works. Very limited functionality so far.  

## Pending Steps  

- Finish detailing file in this readme
- Significant refactoring and reorganization into a usable module instead of a mess of notebooks.
  - Refactor scraping to be faster and more complete  
  - Refactor classification to work on batches of images so the model isn't being spun up for each image individually

## Enhancements
- Model
  - Create an object detection model to find glyph addresses of any size and color on images of any size
  - Refactor preprocessing to only extract square glyph images (in color or grayscale rather than B/W)
- Dash App
  - Flesh out dash app into a functional web app 
    - Add explanatory text divs about project
    - Implement callbacks to view different aspects of data 
    - Make dash app responsive and mobile/tablet friendly
    - Figure out a way to make the galaxy map plot usable on mobile with touch or switch to some other visualization on mobile devices

# Can someone else work on this project? 
No (tentative)  

I plan to continue playing with this and may eventually make it available to other players in the community. 

It is likely that I will get busy or find something else to work on though. If somebody were interested in continuing the project, I might be persuaded to hand it off. 


# Public Display/dissemination
None as of yet.  

# License  
TBD