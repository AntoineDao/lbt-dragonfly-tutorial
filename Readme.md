---
title: Dragonfly Tutorial Series
date: '2018-03-27'
featuredImage: 'https://images.unsplash.com/photo-1511974035430-5de47d3b95da'
excerpt: >-
  This tutorial series will cover the use of ladybug-tools Dragonfly library in a native python ecosystem (no grasshopper required). It should serve as a good basis to better understand the Urban Heat Island effect as well as get used to the Dragonfly API.
---

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/AntoineDao/parametric_dragonfly_poc/master)

You can run this code online for free by clicking on the button above. Embrace the joys of [Binder](https://mybinder.org/).

This is the first post in a series of tutorials on how to model Urban Heat Islands and provide design solutions to mitigate their negative impact on humans and their environment. This series is addressed to urban designers and urban design afficionados who want to learn a bit more about the topic and maybe pick up a few python skills.

We will be mainly using the Dragonfly library by Ladybug Tools to carry out modelling.

### Dependencies
Be sure to have the following packages installed:
* ladybug
* dragonfly
* uwg
* pandas
* seaborn

You can do so using the following command:
```console
pip install lbt-dragonfly pandas seaborn
```
or
```console
pip install -r requirements.txt
```

You will also need to install jupyter (`pip install jupyter`).

Pro tip: you can skip this step by using Binder (click on the tag at the top of this readme).


# Urban Heat Island?

The Urban Heat Island effect refers to the environmental conditions in most urban or metropolitan areas being significantly **warmer** than surrounding rural areas because of human activities. This phenomenon was first reported by Luke Howard, a British chemist and meteorologist, in the early 19th century. Temperature increases are more striking at night and when the wind velocity is low. Furthermore seasonal difference are also observed: for temperate climates the difference in temperature is more extreme in winter, especially in snowy regions, and for tropical regions with a distinct dry and wet season the temperature differential is more dramatic during the dry season.

Check out the image of New York in July and see for yourself if you can discern where vegetated areas are (*cough* central park *cough*).

<div style="text-align:center"><img src ="https://upload.wikimedia.org/wikipedia/commons/4/43/Newyork_heat_island.jpg" /></div>

## Known Impacts
UHIs have impacts on many levels of the environment, from local water systems to urban energy loads and global climate change. 

* **Heat Stress** - The most obvious impact of the UHI effect is the thermal stress imposed on local inhabitants, which is compounded by the fact urban areas generally increase the magnitude and duration of heat waves. 
* **Morbidity** - An increased risk of fatality by causing heat stroke, heat exhaustion or heat syncope is also observed, especially within sensitive risk groups (young children, pregnant women and the elderly). 
* **Cooling Energy** - Higher temperatures naturally increase the need for cooling energy. In the case of cities like Los Angeles where the demand for electric power increases by 2% per degree Fahrenheit, [it is estimated 1-1.5 GW of power is used to compensate the impact of the UHI](https://web.archive.org/web/20090311050754/http://eetd.lbl.gov/heatisland/EnergyUse/).
* **Pollutant Concentration** - Urban areas are also recognisable by their higher concentration of air pollutants of various kinds, which combined with a higher average temperature increases the rate of Ozone production. This in turn will have nefarious effects on the urban biosphere. 
* **Water Systems** - UHI also has an effect on urban water systems as surface water runoff having entered into the sewer system is released into streams with a higher body temperature due to hot pavements and rooftop. 

## Root Causes
The root causes for UHI lie in the changes urban design imposes on its local environment. 

* **Albedo** - Concrete, asphalt and steel significantly reduces the albedo of the urban surface, which results in increased radiation absorption into this same surface. 
* **Reflectivity** - Glazing and the particular geometry of cities into Urban Street Canyons, which reflects radiation  back into the urban space. 
* **Thermal Bulk** - Materials composing the urban fabric generally have high thermal bulk, which means they can absorb more heat during the day that will then be rejected at night. 
* **Anthropomorphic Heat** - Human activity also contributes to increased temperature through heat rejection from vehicles, air conditioning units etc… 
* **Evapotranspiration** - Lack or greenery (trees and grass) in urban areas reduces the amount of evapotranspiration, which increases heat retention. 


# The Pitch
If I have done my job right you should be feeling pretty bummed out about Urban Heat Islands and thinking to yourself: 

* Ok great but just how much greenery do I need to add to my neighborhood to actually have an impact? Will adding a few plants to my balcony do?

Some additional questions you might ask yourself are: 

* What if we paint all our buildings white? Won't that mean all the radiative energy gets sent back right into the atmosphere?
* What if we replace all car traffic with bicycles? Won't that cut a significant amount of anthropogenic heat?
* What if we make buildings more energy efficient so they reject less heat? Now THAT will cut some heat right?
* What if we changed the heights of buildings so urban canyons keep less heat? 

And more importantly you will eventually get to:
* As an urban designer/urban design afficionado how do I decide which of these design decisions will be useful?
* How can I even predict this?

The short answer is I'm not sure... 

However I would like to take you on a a little adventure into the heart of Dragonfly, Ladybug-tools' latest bug, designed to assist in the modelling of urban climate and energy consumption. Through a series of blog posts/tutorials I will show you how to:

1. Model an urban district with Dragonfly and run an Urban Heat Island Simulation
2. Run a parametric study of your district to inform the design of urban areas 
3. Deploy Dragonfly to the "Cloud" (AWS Lambda) to run monstrous amounts of parametric simulations in a realistic timeframe
4. Use alternative sources of data to create your models (Open Street Map, GeoJSON etc...)

Please be aware that I am currently writing these tutorials on the side of real life work so might not be able to churn them all out in one go. I expect to be done with this series by the end of January 2019. Extra Github stars, comments and words of encouragement will always be welcome and help me write these out quicker.
