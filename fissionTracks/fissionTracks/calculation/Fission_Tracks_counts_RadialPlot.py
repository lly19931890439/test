#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import rcParams
from pyRadialPlot import radialplot

rcParams["figure.dpi"] = 300


# The radial plot is a graphical method for displaying and comparing observations that have different precision. Invented by Rex Galbraith in 1988 it is commonly used in geochronology but as also a wide range of applications in business analytics or medical research. The observations are standardised and plotted against precision, with the precision defined as the reciprocal of the standard error. The original observations are given by slopes of lines through the origin and can be read using a circular scale. Radial plots provide a visual representation that can help to assess whether the estimates agree with a common value. They can also be used to identify outliers or groups of estimates differing in a systematic way because of some underlying factor or mixture of populations.    
# 
# In experimental sciences it is common to have measurements with different precision. This can arise from natural variations or from the experimental procedure. Geochronological methods such as fission track, $^{40}\text{Ar}/^{39}\text{Ar}$, U-Pb and Optically Stimulated Luminescence (OSL) dating produce age estimates and associated errors for each of several grains. The radial plot can be used to display and compare the age estimates and see how they agree or differ within standard statistical variation.
# 
# Another application of radial plot is in *meta-analysis*. Radial plots can be used to compare treatments effects from different clinical studies where the precision of the studies varies.

# In[2]:


# ax = radialplot(file="ressources/FTdata.csv", transform="arcsine")


# In[5]:


ax = radialplot(file="ressources/2.csv", transform="logarithmic")


# In[4]:


# ax = radialplot(file="ressources/FTdata.csv", transform="linear")

