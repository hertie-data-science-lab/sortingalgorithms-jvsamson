[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Trv1ybv1)
# Sorting Algorithms

## Assignment:

A Bucket sort can use any stable sorting algorithm to sort the elements in its buckets.
It can also recursively sort the elements in its buckets into smaller buckets. This is useful when the buckets are still large and unsorted after the first pass of a bucket sort.
Rewrite the bucket sort algorithm to call itself until each bucket contains only one element or is already sorted by another algorithm (you may use any stable sorting algorithm).

* You may use the code provided in this repository as a starting point.
* You may choose to edit bucket.py or copy the contents into a new file. either way, let me know which is your final submission.
* [Document](https://realpython.com/documenting-python-code/) your code and use [modular programming](https://realpython.com/python-modules-packages/#executing-a-module-as-a-script) to maximise the quality of your code.


## Additional Notes

* Please do not double-submit. If you are part of a group, do not submit a separate assignment as well.
* List your group members in the README file or in the header for your submission.
* Submit by May 8 at 12 am.

## Solution:

Our final submission is in the file 'bucket_recursive.py'. We have reworked the original bucket sort algorithm to call itself recursively until each bucket contains only one element or is already sorted by another stable sorting algorithm. We have used modular programming and provided documentation throughout the code to maximize the quality of our work.

### The 'bucket_recursive.py' file includes:
- The `bucketSort_recursive` function, which is our modified recursive bucket sort algorithm.
- A test function with various test cases, including positive, negative, decimal, zero, and duplicate values, to demonstrate the functionality of the algorithm.
- A docstring for the `bucketSort_recursive` function, explaining its purpose, parameters, return values, and modularity despite having the test function in the same file.


## Authors

- Benedikt Korbach ([benedikt-korbach](https://github.com/benedikt-korbach))
- Niklas Pawelzik ([nikpaw](https://github.com/nikpaw))
- Justus von Samson-Himmelstjerna ([jvsamson](https://github.com/jvsamson))
- Alvaro Guijarro ([Alvaroguijarro97](https://github.com/Alvaroguijarro97))
