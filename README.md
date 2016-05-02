# Champion Affinity ([live site](http://champion-affinity.getforge.io/))

For [Riot's API Challenge (2016)](https://developer.riotgames.com/discussion/announcements/show/eoq3tZd1), we decided to explore how the mastery data provided by the Riot API can model the relationships between champions. For example, if a summoner enjoys playing Garen, how does that predict whether they would enjoy playing Annie? This sort of data could be useful to find new champions to expand your champion pool with, or for designers, identify champions that don't have an obvious progression to another champion. We've generated a few metrics to explore this idea, using an initial population of Masters/Challenger players. You can read more about how each metric is calculated below (or on the site's [about](http://champion-affinity.getforge.io/about) page)

We've built multiple visualizations using some or all of our metrics. The purpose of multiple visualizations is to show how much the visualization matters when presenting data; depending on how you display data, you could learn completely different things! On each page, we'll also talk about some of our initial insights based on each visualization.

In this README, we'll go through the design decisions for each part of the application; the design of the site, the visualizations, and the backend processing.

Champion Affinity was designed and created by [Chris](http://theisencr.github.io/) ([Ellipson (NA)](http://na.op.gg/summoner/userName=Ellipson)) and Rob ([T3lrec (NA)](http://na.op.gg/summoner/userName=t3lrec))

Chris designed the metrics, did the development work, and wrote most of the words you're reading here and on the site itself.

Rob acted as a sounding board for ideas (including many late nights in Discord/Hangouts), helped design the color scheme, and provided proofreading and feedback on the final application. 

##Site Design
