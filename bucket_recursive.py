# -*- coding: utf-8 -*-
"""
Created on Sun May  7 16:37:20 2023

@authors:
- Benedikt Korbach (GitHub: benedikt-korbach)
- Niklas Pawelzik (GitHub: nikpaw)
- Justus von Samson-Himmelstjerna (GitHub: jvsamson)
- Alvaro Guijarro (GitHub: Alvaroguijarro97)
"""


def bucketSort_recursive(array):
    # Find minimum/maximum values in input array:
    # Find minimum in input array
    min_val = min(array)
    # Find maximum in input array
    max_val = max(array)

    # Calculate value range and size of each bucket
    # Calculate value range in input array
    value_range = max_val - min_val
    # Determine number of buckets to create
    num_buckets = len(array)
    # Create an empty bucket for each element in input array
    bucket = [[] for _ in range(num_buckets)]

    # Insert elements into their respective buckets
    for j in array:
        # Calculate bucket index j should be placed in
        index_b = int((j - min_val) / value_range * (num_buckets - 1))
        # Add j to corresponding bucket
        bucket[index_b].append(j)

    # Sort  elements of each bucket recursively
    for i in range(num_buckets):
        # Check if bucket has more than one element
        if len(set(bucket[i])) > 1:
            # Recursively sort elements of the bucket
            bucket[i] = bucketSort_recursive(bucket[i])

    # Return the sorted elements of the input array
    return [element for sublist in bucket for element in sublist]


# Test function with positive, negative, decimal, zero, duplicate
array = [3, 1, 4, 1, 5, 9, 2, 6, 5.4, 3, 5, 5.5, 5.52, -3, 0, 0, 1000]
sorted_array = bucketSort_recursive(array)
print("Original Array:", array, ", \n", "Sorted Array:", sorted_array)
