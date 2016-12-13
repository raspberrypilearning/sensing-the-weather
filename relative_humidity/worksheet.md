# Sensing the Weather - Relative Humidity Worksheet

In this lesson you will:

- Be able to take temperature and relative humidity readings from the relative humidity sensor
- Be able to write code to solve a given equation for a chosen variable
- Be able to look up values in a dictionary and return a corresponding statement

## How does the relative humidity sensor work?

Here is the relative humidity sensor component on the air board included with the Raspberry Pi Weather Station. The component is circled in red. (The relative humidity and ambient temperature are both measured by the same sensor.)

![Relative Humidity Sensor](images/air_board.png)

## How does it work?

This sensor detects both the ambient temperature and the relative humidity of the air surrounding it. 
These types of sensor detect changes in temperature and humidity in two possible ways depending on how they are built.

**Capacitive sensing** - The sensor uses a material which absorbs water from the air. The sensor's capacitance (ability to store an electric charge) changes depending on how much water vapour the air contains, and this can be measured and converted into meaningful units.

**Resistive sensing** - The sensor uses a material which has the property that its resistance (how easy it is for a current to pass through it) changes depending on the humidity of the surrounding air, and this value is measured and converted into meaningful units. 


## Reading relative humidity data

Reading data from the relative humidity sensor is almost identical to the code we used to read from the ambient temperature sensor - because the sensor is the same component!

```python
import HTU21D as temp_humid

humidity_sensor = temp_humid.HTU21D()

current_humidity = humidity_sensor.read_humidity()
print( str(current_humidity) + "%")

```

Type in this code and check that your humidity sensor is giving a reading. If you are testing your code indoors, the value will probably be approximately between 30 and 50%.

## Calculating the dew point

### Question
What is the dew point, and why is it important?

### Answer
The dew point is the temperature at which the water vapour in the air will condense to form liquid dew. It is important to be able to measure the dew point in lots of situations. If the dew point temperature is reached indoors this will result in condensation and cause mould and mildew to grow, affecting people's health. If the dew point is negative (sometimes called the **frost point**) and the air temperature equals the dew point, this will result in the water vapour freezing and causing a frost. 

We can calculate the dew point using a formula called the **Magnus formula** - here is the code:

```python
dew_point = ((humidity / 100) ** 0.125) * (112 + 0.9 * temperature) + (0.1 * temperature) – 112
```
1. Create a new python file called `calculate_dewpoint.py`. Write a program to calculate and display the dew point using readings from your sensor. Store the relative humidity reading as `humidity` and the ambient temperature reading as `temperature`

	If you would like to check your answer, the finished code is [here](code/calculate_dewpoint.py)

1. People find the environment to be comfortable or uncomfortable depending on the dew point temperature. This [Wikipedia page](https://en.wikipedia.org/wiki/Dew_point) has a table of dew point thresholds and what they feel like to a human. We are going to put these into a data structure called a **dictionary** and display a message relating to the current dew point value. 

1. Here is an example dictionary of test score thresholds:

	```python
	test_scores = 	  {  0 : "F",
	                    20 : "E",
	                    40 : "D",
	                    50 : "C",
	                    70 : "B",
	                    80 : "A",
	                    90 : "A*" }
	```

	In this example, the numbers represent the score gained and are called the **keys** of the dictionary. The letters represent the grade that corresponds to that key and they are called the **values** of the dictionary.

	We can generate a list of all of the **keys** and sort it into ascending order:

	```python
	grade_boundaries = list( test_scores.keys() )
	grade_boundaries.sort()
	```

	Given a student's score, we will now look through this list to find out which grade they should be awarded, and we will store the highest boundary they passed in the variable `highest_boundary`

	```python
	student_score = 75

	highest_boundary = 0
	
	for score in grade_boundaries:
	    if student_score > score:
	        highest_boundary = score
	```

	Now we can go back to the dictionary and print the **value** of the highest boundary they crossed, using the `highest_boundary` variable as the **key**

	```python
	print( test_scores[highest_boundary] )
	```

	Result: `B`

	Start a new Python file called `grade_boundaries.py` and type in the code. Try changing the variable `student_score` to other values to check that the correct grade is awarded.

1. Switch back to your `calculate_dewpoint.py` program. Using the code above to help you, create a dictionary of the following threshold values for dew point feelings:

| Threshold &deg;C  | Message           		|
| -----------------	| --------------------------| 
| 0      			| A bit dry for some 		| 
| 12      			| Very comfortable      	|   
| 16 				| Comfortable      			|    
| 18 				| Upper edge of comfortable |  
| 21 				| Somewhat uncomfortable    |  
| 24 				| Quite uncomfortable      	|  
| 26 				| Extremely uncomfortable  	|  
| 27 				| Severely high to deadly  	|  


1. Find the largest threshold crossed by your dew point value and store it in a variable.

1. From the dictionary, print the correct corresponding statement for the dew point you calculated. 

1. Run and test your code. You can check your answer using the [dew point calculator](http://www.ajdesigner.com/phphumidity/dewpoint_equation_dewpoint_temperature.php#ajscroll)

	The finished code is [here](code/calculate_dewpoint_message.py) for you to look at

## Summary

- You have created a program which reads two data points from a sensor and uses a known equation to calculate the dew point
- You have used a dictionary to look up your value and display a corresponding message

## What's next

- Could you make a dew point calculator - allow the user to input their own values for temperature and relative humidity and give them the dew point
- Could you add a GUI to your dew point calculator?