#  Weather Station Basic I/O - Lesson Plan 5

In this lesson students will complete their initial work on the weather station using the rain gauge and the anemometer. They will work to combine elements from the 2 programs created  for these sensors into 1 single program to manage them both.

## Learning objectives

- To demostrate an understanding of how their programs work, by combining them.
- To use code annotation to explain the function of sections of code.
- To debug errors to create a working solution

## Learning outcomes

### All students are able to

- Explain the function of some key lines of code
- With support combine their programs into 1 solution.

### Most students are able to

- Clearly explain the function of the majority of c the code
- Combine their programs into 1 solution, including some commenting.

### Some students are able to

- Clearly explain what each line of code does and how they work together
- Independently create a program which combines the 2 functions from previous lessons, complete with commenting.

## Lesson Summary

- Code review of the previous 2 solutions.
- Group discussion around challenges involved in merging programs.
- Students create single solution and annotate it.
- Students review each other's code and annotation.

## Starter

Share with the students the code for [anemometer](../lesson-4/code/wind_final.py) and the [rain_gauge](../lesson-4/code/rain_interrupt.py). Students are invited to explain what the 2 programs are doing and how they are working. This could be done by:
- Class discussion, which notes being made somewhere.
- Projecting code onto a whiteboard, students use sticky notes to add annotation.
- Printed copies which students individually annotate.
- Google doc / [Classroom](classroom.google.com)

## Main development

### Identifying Challenges

Explain to students that their challenge today is to combine these 2 programs together to create a single solution. The solution should measure and report both rainfall and windspeed every 5 seconds (or at an interval of their choosing). Ask the to consider what approach they might take and to consider the following:

- Some lines of code occur in both programs and would only need to occur once.
- Some variables (count,pin etc) in the programs are the same, would this cause a problem.
- Each program has a set of defined functions, these need to be defined at the beginning of the program before they are used.
- Both programs contain a loop of some kind to display the current readings, these will need to be combined.

### Importance of Comments
Show the students how to add comments to their code, a line proceeded by a `#` symbol is ignored by the computer and provides a useful comment. eg

  ```python
#The spin function is called whenever a spin is detected
#it increments the count variable and print it out

def spin(channel):
  global count
  count = count + 1
  ...
```

Ask the students what purpose comments serve when writing a program?
- They help explain the intended function of the programmer,to others that might read the code, looking for ideas or to improve it.
- Comments help the programmer keep track of what their code is doing and make it easier to return to a piece of code and still make sense of it.

### Solution Development

Students should be given time to build their own solution which logs and displays both rainfall and windspeed. Their solution should be well annotated and tested to ensure functionality.

- They may want to set up their pi with a weather station / buttons for testing.
- They could either start with a blank file and write from scratch or start with 1 program and incorporate the other.
- Decide to what extent you want the students to collaborate, even if they help each other they will likely end up with subtley different solutions. Emphasise the fact that their is no single correct solution.

## Plenary
Students should be given chance to review each others code and comments. They should be providing feedback, advice and comment on whether they each have a working soluution.

Spend a moment reviewing the concepts they have covered in this scheme and to what extent they understood and applied them.

-

## What's Next?
- Students could use this code to deploy a basic version of the weather station which displys data on rainfall and wind speed.
- Consider what's missing from this solution, clearly only 2 of the sensors have been covered but what else?
    - Is this the best way to display the data?
    - Is data being saved, could I look back at previous data?
