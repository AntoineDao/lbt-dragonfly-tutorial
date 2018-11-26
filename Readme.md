# Parametric Dragonfly Proof Of Concept

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/AntoineDao/parametric_dragonfly_poc/master)

You can run this code online for free by clicking on the button above. Embrace the joys of [Binder](https://mybinder.org/).

## Quick Intro
This gist is a quick proof of concept on how to carry out a parametric Urban Heat Island simulation for a neighborhood using some interpreted geometric data and a weather file.

The input data for the baseline neighborhood design was provided by running dragonfly in rhino on geometry for a neighborhood of Malaga called La Luz.

It's worth noting that quite a few aspects of this study are not perfect in my opinion (eg: focusing on one month of averaged data to determine the impact of different parameters on the UHI of an area is pretty uninteresting). Were I a better man I would have run some fancy stats to asses those impacts by removing seasonality.
Another interesting thing to note is that having tried a similar simulation on another epw for Malaga the UHI effect is not as striking. It would be interesting to look into the impact of an EPW on UHI compared to the other District level inputs.


## Running the gist
### 1. Dependencies
Be sure to have the following packages installed:
* ladybug
* dragonfly
* uwg
* pandas
* seaborn
* jupyter

You can do so using the following command:
```console
pip install lbt-dragonfly pandas seaborn
```
or
```console
pip install -r requirements.txt
```

### 2. Running the simulation
Open the `UHI_calcs.ipynb` file with jupyter and run the cells. Definitely read before you press run on all (the parametric part takes 7-10 hours to run...)

### 3. Analysing the data
Open the `Weather Data Analysis.ipynb` file with jupyter and run the cells. You can go nuts and run all of them if you feel like it this time.

## Conclusion
Hope this is interesting to some, maybe even fun (?!). Please drop an issue in this repo if you're having trouble running this on your machine and have tried googling for more than 10-15 mins.

PS: here's a topical comic from xkcd

![xkcd on global warming](https://imgs.xkcd.com/comics/4_5_degrees.png)
