# -*- coding: utf-8 -*-
"""Python_Libraries_Advanced.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LnGOVQ5tJDChpdKaKdMNhDI669giE9TU

# Introduction to NumPy, Pandas, Matplotlib and Seaborn, and Sci-Kit Learn
"""

#@title Run this to prepare your data! { display-mode: "form" }
import gdown
gdown.download('https://drive.google.com/uc?id=1eDhwxZxEnMoKcaR-ATW21ReuKdwpMdrF', 'airline-safety.csv', True);
gdown.download('https://drive.google.com/uc?id=14FYQvB05JqfU4d1Wn1LSv_Jh0om7AI0M', 'tips.csv', True);

"""Before we set out on our journey into the land of artificial intelligence, we must first pack some gear.
Some of the essentials include Numpy, Pandas, Matplotlib, and Seaborn. Let's discuss Python Packages first!

### Note: In case of time constraint, only do the sections that have an emoji next to the title.

## What are Python Packages?

A Python package is simply a collection of modules — files consisting of Python code. The packages that we'll be looking at today include Numpy, Pandas, Mathplotlib, and Seaborn. Let's begin with NumPy.

# NumPy: An Introduction  🤖

Numpy is the core library for scientific computing in Python. Numpy provides the flexibility to create multidimensional array objects (arrays within arrays) and compute a wide variety of mathematical operations including basic linear algebra, basic statistical operations, random simulation and much more. We will represent all of our data which will be fed into our machine learning models using Numpy.

We'll start with the standard NumPy import, under the alias np:
"""

import numpy as np

"""### Arrays 🚖

An **array** is simply a collection of items. At the heart of a Numpy library is the array object or the ndarray object (n-dimensional array).  Simply put, it is a table of elements (usually numbers and the same type) indexed by a tuple of positive integers. In NumPy dimensions are called **axes**. The number of axes is referred to as **rank**.
<br/>
Let's create an 1D array of  **taxi rates** (in dollars) by passing it through a list:
"""

a = np.array([12.50, 10.20, 25])

"""We can view the contents of the array by running the following code:"""

a

"""Awesome! 👏 Let's now create an multi-dimensional array."""

b = np.array([
    [19.50, 13, 12, 11 ],
    [12.50, 10, 25, 14]])

b

"""## Exercise 1:  Arrays ⛷

Time for our first exercise!
- Create a NumPy single - dimensional array and assign it to a variable that describes the following situation:
    - Find the weather for the next 5 days in your favorite city, and enter it into the array.
- Create another NumPy single - dimensional array and assign it that describes the following situation:
    - Write your 5 favorite numbers.
- Can you try adding the two arrays? How about subtracting?
"""

# YOUR CODE HERE #

"""### Methods ⛵️

🎉 Let's now explore some of the methods in NumPy. The [**.shape**](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.shape.html) method for nparray returns the dimensions of the given array. For example, [x].shape returns the (vertical, horizontal) dimensions of the variable x. Let's use .shape to find the dimensions of the multi-dimensional array that we've created above:

_Can you guess the shape before running the command?_
"""

b.shape

"""Note that multi-dimensional arrays can also have more than two dimensions. A three-dimensional array, for example, has arrays within arrays within arrays. Calling array.shape on a 3-dimensional array would return three numbers: (num1, num2, num3).

**Make sure you understand the concept of shapes because this will come up again and again throughout your machine learning experience!**

The [**.linspace**](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html) method is used to return evenly spaced numbers over a specified interval. Let's create an array of 6 integers between 0 and 100 to demonstrate this method:
"""

np.linspace(0,100,6)

"""How about if we wanted to decide the step? The [**.arange**](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html) method allows us to return evenly spaced values within an given interval."""

np.arange(0,10,3)

"""Yay! 🙌 What if we didn't want to define the interval or the step? The [**.random.rand**](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.rand.html) method accomplishes this purpose by creating an array of a specified shape and fills it with random values. Let's create a 4 x 5 array of random floats between 0-1:"""

np.random.rand(4,5)

"""If we want to increase the size of the floats between an certain interval (0-100), we can simply multiply by the highest digit in that interval:"""

np.random.rand(4,5)*100

"""Notice how the numbers when you call the random function are different the second time. This is because it generates new numbers each time.

We can also explore some of the properties of the array. The [**.dtype**](https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html)  method outputs the type of elements in an given array:
"""

c = np.arange(0,10,3)

c.dtype

"""Kudos! **int64** simply means that the elements in the array are integers. Remember that NumPy arrays only support an *singular* data type for each array unlike Python arrays. Other data types include **float64** and **double64**, which are used to specify numbers with decimals (**int64**s must be whole numbers).

## Exercise 2: Methods 🏃

Time to test our skills!

- Using the **.shape** method, find the dimensions of the array containing the weather of your favorite city.
- Use the **.linspace** method to create an array of 5 evenly-spaced integers between 15 and 45
- Create a 3x6 array using the **.random.rand()** method
"""

# YOUR CODE HERE #

"""## Operations

NumPy offers the ability to compute arrays together.
"""

x = np.array([3,4,5])

y = np.array([1,2,3])

"""We can use traditional math symbols to add, subtract, multiply, and divide the two arrays:"""

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x**2)

"""## Scalar Math

We can use basic functions to add, subtract, multiply, divide, and power the array:

_Can you guess the output before running command?_
"""

np.add(x,1)

np.subtract(x,2)

np.multiply(x,3)

np.divide(x,4)

np.power(x,5)

"""## Indexing, Slicing and Reshaping 🔭

Now, we're going to explore some of the functions in Python. First, let's create an array with 12 numbers using the **arange** method in increments of 5:
"""

s = np.arange(12)*5 # note this is same as np.arange(0,12,1)*5
s

"""**Indexing** refers to retrieving a specific element of an array. Let's find the 3rd value in the above array:"""

s[2]

"""**Note**: The values of an array always start with x[0]. We can also retrieve values within an certain range using the **:** symbol:"""

s[2:5]

"""😎 Now, let's try combining two arrays using [**concatenate( )**](https://docs.scipy.org/doc/numpy/reference/generated/numpy.concatenate.html) and add 'a' as rows to the end of 's':"""

np.concatenate((s,a))

"""🙌 How about splitting arrays? We can use the [**.split()**](https://docs.scipy.org/doc/numpy/reference/generated/numpy.concatenate.html) method to split the s array in sub-arrays:"""

z = np.arange(9.0)
z

split_arr = np.split(z, 3)

split_arr

"""**What do y'all think the shape of the above array is?**"""

np.array(split_arr).shape

"""## Exercise: Indexing, Slicing and Reshaping

Time for a test!

- Using the **arange** method, create an array of 5 numbers in increments of 10. Call it 'oreo'
- Retrieve the 3rd number in the above array named 'oreo'
- Create another array of 5 numbers in increments of 15. Use any method you like and call it 'milk'
- Retrive the 1st number in the above array named 'milk' <br>
Can you eat those many oreos and drink that many cups of milk? You decide! 🥛
"""

# YOUR CODE HERE #

# YOUR CODE HERE #

# YOUR CODE HERE #

# YOUR CODE HERE #

"""😀 We've completed our review of NumPy! After you take a quick break - walk around, drink water - let's move on to Pandas.

# Pandas: An Introduction 🐼

Pandas is an open source Python package that provides numerous tools for data analysis. Pandas provides </br> fast, flexible, and expressive data structures designed to make working with structured (tabular, multidimensional, potentially heterogeneous) and time series data both easy and intuitive. It aims to be the fundamental high-level building block for doing practical, real world data analysis in Python.

We'll take look at some of the core ideas in Pandas here. You can learn more about Pandas in their official [documentation](http://pandas.pydata.org).

## [Pandas Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html) ❄️

A **Series** is similar to an one dimensional array and can store data of any type. The values of a Pandas Series are mutable but the size of a Series is immutable and cannot be changed.<br>
The first element in the series is assigned the index 0, while the last element is at index N-1, where N is the total number of elements in the series.

Let's first **import** pandas under the common alias **pd**:
"""

import pandas as pd

"""### Creating a Pandas Series

We can create a series by invoking the pd.Series( ) method, like this:
"""

decades = pd.Series(np.array([10,20,30,40,50,60]))

decades

"""As shown above, the index is assigned values from 0-5.

## Exercise: Pandas Series🎿

Exercise time!

- Create a Series for the lowest GDP's in the world:
    - Czech Republic: 264.50
    - Iraq:	250.07
    - Romania: 248.84
    - Portugal:	242.83

Tip: See what arguments are available in [pd.Series](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html) and use the countries as the index.
"""

# YOUR CODE HERE #

"""## [Pandas DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) 🐨

The DataFrame is similar to a table. It organizes data into rows and columns as an two-dimensional data structure. The columns can be of different types, and the size of a DataFrame is modifiable. <br>
Let's create a DataFrame of 14 animals, populated with age, weight, and length. <br> First, let's create a Python dictionary.
"""

animal_dict = {
     'Animal' : ["Hamster", "Alligator", "Hamster","Cat", "Snake", "Cat","Hamster", "Cat", "Cat", "Snake", "Hamster", "Hamster", "Cat", "Alligator"],
     'Age' : [1,9,4,13,14,10,2,4,14,7,14,2,1,7],
     'Weight': [7,13,8,12,11,8,10,14,9,11,10,10,9,14],
     'Length' : [8,6,9,1,8,9,5,6,6,6,5,3,4,5]
}

"""Now, let's turn our Python dictionary into a DataFrame:"""

animal = pd.DataFrame(animal_dict)
animal

"""We turned a dictionary into a dataframe! Can you tell which parts of the dictionary became the headers and what became the values?

### Pandas Methods 🐢

Great! 👍 Pandas has many unique methods that we can use for data analysis and filtering. Let's first explore [**.unique( )**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.unique.html). This method returns all the unique values in an given series or column:
"""

pd.unique(animal["Animal"])

"""Let's now look at the [**describe()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.describe.html)  method. This method returns the summary statistics of numerical columns. To return the numerical statistics, we write:"""

animal.describe(include=[np.number])

"""Super simple! 🥳  **np.number** simply returns the numerical columns and excludes other data types. Now, let's attempt to filter columns in Pandas. <br>
To filter in Pandas, we simply use brackets. Let's try one example:
"""

animal[animal["Weight"] > 10]

"""🐍 Python is wonderful because it's so intuitive. We pointed to **animal**, and then to the **"Weight"** column. At this point, we filtered for numbers greater than 10
.

What if we want to find rows between a certain subset? We can use the '&' operator:
"""

animal[(animal["Length"] > 4) & (animal["Length"] < 8)]

"""We are almost finished our review of Pandas DataFrames. 🤠 Let's now turn our attention to [**.groupby()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html). The Groupby method involves grouping data around a particular category and applying analysis. This would be useful if you were interested in answering the question, "What's the average weight of all the snakes, cats, hamsters, and alligators?" To find the average weight of each category of animal, we'll group the animals by animal type and then apply the mean function. We could apply other functions too. We could apply "sum" to add up all the weights, "min" to find the lowest, "max" to get the highest, or "count" just to get a count of each animal type:"""

animal_groups = animal.groupby("Animal")
animal_groups['Weight'].mean()

"""## Exercise 3: DataFrame 🏃
- Open the [UN Dataset](http://data.un.org/_Docs/SYB/PDFs/SYB60_T03_Population%20Growth,%20Fertility%20and%20Mortality%20Indicators.pdf)
- Create a DataFrame using **Northern Africa**, **Sub-Saharan Africa**, **Eastern Asia** and **Western Europe**. For these areas, create columns for *Population Rate of Increase*, *Fertility Rate*, and *Infant Mortality* for the year 2005.
- Using filtering, sort for the countries that have infant mortality between 30 and 50.
- Find the max for Infant Mortality for the four areas
"""

# YOUR CODE HERE #

# YOUR CODE HERE #

# YOUR CODE HERE #

# YOUR CODE HERE #

"""With that, we've completed our review of the Python library Pandas. If you have any lingering questions, do ask! You can find more on Pandas on their [official website](pandas.pydata.org).

# Matplotlib: A (Tiny) Introduction 📈

Mathplotlib is a Python 2D plotting library which produces  plots, histograms, power spectra, bar charts, errorcharts, scatterplots, etc. with just a few lines of code. Source: [Matplotlib](https://matplotlib.org). <br>
We'll cover only some of the coolest features in this Notebook due to time constraints. You can explore more on the [official website](https://matplotlib.org/tutorials/index.html)

Let's import the `mathplotlib` library under the alias `plt`
"""

import matplotlib.pyplot as plt

"""### Pyplot

Pyplot is a module of Matplotlib which provides simple functions to add plot elements like lines, images, text, etc. to the current axes in the current figure.

We'll import the Pyplot module to create a simple plot. We will be using two NumPy arrays - one for the x-coordinates and another for the y-coordinates:
"""

plt.plot([1,2,3,4],[1,4,9,16]) # plt.plot([x-coordinates], [y-coordinates])
plt.show()

"""Now, we can add titles, and labels:"""

plt.plot([1,2,3,4],[1,4,9,16]) # plt.plot([x-coordinates], [y-coordinates])
plt.title("First Plot")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.show()

"""Another commonly used graph in Machine Learning is the Scatter Plot. Let's create a basic scatterplot in MathPlotLib comparing the distribution of height vs. weight:"""

height = np.array([167, 170, 149, 165, 155, 180, 166, 146, 159, 185, 145, 168, 172, 181, 169])
weight = np.array([86,74,66,78,68,79,90,73,70,88,66,84, 67, 84, 77])

#We can set the limit (lower, upper) for the x-axis and the y-axis using xlim and ylim, respectively.
plt.xlim(140, 200)
plt.ylim(60,100)
#A scatterplot can be generated through .scatter(x,y)
plt.scatter(height,weight)
plt.title("Comparing Height vs. Weight")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()

"""## Exercise: MatPlotLib 🏃

- Using the data for the animal weights and lengths, create an scatterplot comparing the information.

Note: Remember to properly label the graph (x-axis, y-axis, and title!)
"""

# YOUR CODE HERE #

"""# Seaborn: Another (tiny) introduction 🌊

Let's first import the library for seaborn under the alias sns:
"""

import seaborn as sns

"""Let's import a csv file - comma-seperated values - that details the total bill costs and the tips. We'll run a scatterplot on this data:"""

# Run this code to import the data and read it in using 'pd.read_csv('file')'
tips = pd.read_csv('tips.csv')
ax = sns.scatterplot(x="total_bill", y="tip", data=tips) #plotting it

"""The scatterplot above does not discriminate between the days of the week. What if we wanted to see the distribution of the data for each day?
<br>
For this, we can consider using a categorical scatterplot with the **.catplot()** method.
"""

sns.catplot(x="day", y="total_bill", data=tips);

"""We can go even further! How about we try sorting the time of the day that the customer dined at the restaraunt? Let's use the swarm parameter to prevent the points from overlapping and group by time:"""

sns.catplot(x="total_bill", y="day", hue="time", kind="swarm", data=tips);

"""To reiterate, the *hue* parameter allows us to add another dimension to group data by color. The *Swarm* parameter helps us to visualize the data more clearly by preventing overlapping points (as opposed to catplot where points with the same data values will lie on top of each other).

## Exercise: Seaborn 🐳

Time for one of our last exercises!

- Create a simple scatterplot comparing size of tip vs. size of table.
"""

# YOUR CODE HERE #

"""# Scikit-Learn: A Small Preview 👀

**Scikit-learn** is a free software machine learning library for the Python programming language. It features various classification, regression and clustering algorithms including support vector machines, random forests, gradient boosting, k-means and DBSCAN, and is designed to interoperate with the Python numerical and scientific libraries NumPy and SciPy. Official website: https://scikit-learn.org/ <br>
We'll be building a simple linear regression in Scikit-Learn to demonstrate how the library works at the base level.

## Sneak Peak: Linear Regression 🏡

Linear regression is a linear approach to modeling a relationship between an response variable and an explanatory variable. We will study this in detail tomorrow!

We'll create a small model that predicts the relationship between expected and true housing prices using the Boston Housing Dataset:

## Import 📦
"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
data = load_boston()

"""### What is this data?"""

# Print the description of the dataset (first 1500 characters)
print(data.DESCR[:1400])

# data.data are all the houses with their attributes.
# data.target are the corresponding house prices

print("House 1, attributes: ", data.data[0])

# Show the actual price for these 2 houses
print("House 1, price: ", data.target[0])

"""## Train and Define 🚂

We're going to define our X-axis and Y-axis and fit the model to a Linear Regression model.
"""

X_train, X_test, y_train, y_test = train_test_split(data.data, data.target)
clf = LinearRegression()
clf.fit(X_train, y_train)
predicted = clf.predict(X_test)
expected = y_test

"""## Plot 📊"""

plt.figure(figsize=(4, 3))
plt.scatter(expected, predicted)
plt.plot([0, 50], [0, 50], '--k')
plt.axis('tight')
plt.xlabel('True price ($1000s)')
plt.ylabel('Predicted price ($1000s)')
plt.tight_layout()

"""Woo! We've just seen a small preview of what Scikit-learn can do. We have the ability to create an accurate ML model with a few lines of code.

We hope you learned something useful, and feel more curious to learn more about AI!
"""