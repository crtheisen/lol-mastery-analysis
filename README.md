# Champion Affinity ([live site](http://champion-affinity.getforge.io/))

For [Riot's API Challenge (2016)](https://developer.riotgames.com/discussion/announcements/show/eoq3tZd1), we decided to explore how the mastery data provided by the Riot API can model the relationships between champions. For example, if a summoner enjoys playing Garen, how does that predict whether they would enjoy playing Annie? This sort of data could be useful to find new champions to expand your champion pool with, or for designers, identify champions that don't have an obvious progression to another champion. We've generated a few metrics to explore this idea, using an initial population of Masters/Challenger players. You can read more about how each metric is calculated below (or on the site's [about](http://champion-affinity.getforge.io/about) page)

In this README, we'll go through:

- The overall structure of the GitHub repository
- How the backend scripts work and the dependencies required to run them
- How the visualizations work
- How the site was built and the dependencies required to deploy it

Champion Affinity was designed and created by [Chris](http://theisencr.github.io/) ([Ellipson (NA)](http://na.op.gg/summoner/userName=Ellipson)) and Rob ([T3lrec (NA)](http://na.op.gg/summoner/userName=t3lrec))

Chris designed the metrics, did the development work, and wrote most of the words you're reading here and on the site itself.

Rob acted as a sounding board for ideas (including many late nights in Discord/Hangouts), helped design the color scheme, wrote text content, and provided proofreading and feedback on the final application.

##GitHub Structure

First, we'll go over the structure of the files in our repository.

###Root

Root contains the following:

- The <code>README</code> you're reading now!
- The python scripts that makeup the backend
- Our verification text file
- The deployable .zip file of our public-facing app

###Data

This folder contains the files that support the creation and evaluation of our metrics. The files on GitHub represent mastery data from Masters/Challenger players and metric calculations from April 25th, 2016. These files can be regenerated using the backend scripts at any time, though some differences should be expected in the final results.

###Static_Data

This folder contains a single file, <code>mobafire-icon-lookup.csv</code>. This file provides some mappings that were generated manually: 
- <code>Name -> Graph_ID</code> for mapping to nodes on our eventual visualizations
- <code>Name -> Mobafire_Name</code> and <code>Name -> Mobafire_ID</code> for generating links to each champion's [Mobafire](http://www.mobafire.com) page
- <code>Name -> Image_ID</code> for looking up each champion's icon.
These mappings are referenced by our backend scripts for generating our data for our final public-facing site.

###Tests

This folder, along with <code>test_controller.py</code> in the root directory, was used to test API calls and make sure the GET requests were formatted properly. Originally, we planned on building a unit test for each individual API endpoint we were referencing, just to explore how the built-in <code>unittest</code> module in Python works. The need to ship something for the contest won out, however.

##Backend (Data Collection and Metric Calculations)

##Visualizations

##Site Design

##Run It Yourself
