#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# You have a warehouse of triangles
# You have a database for this warehouse which contains the dimmensions of each triangle
# the data comes to you in the form of a list of lists where each inner list contains the 3 sides to a triangle

# Write a program which loops over each triangle and determines whether or not it is a right triangle
# The output should be a new list which only contains right triangles


# In[ ]:


"""
a**2 + b**2 = c**2

c = (a**2 + b**2)**0.5

   |\
 a | \  c
   |  \
   |___\
     b
"""


# In[1]:


# Here is the output from your database of triangles

triangles = [
    [3, 4, 5],
    [5, 5, 50],
    [5, 12, 13],
    [1, 3, 7],
    [9, 14, 90],
    [3, 8, 10],
    [2, 7, 9],
    [6, 8, 10]
]


# In[12]:


# STEP1
# write a function which determines whether or not a triangle is a right triangle based on the dimmensions

def check_right_triangle(triangle):
    triangle_copy = triangle.copy()
    
    c = triangle_copy[-1]
    b = triangle_copy[0]
    a = triangle_copy[1]
    
    right_tri = (a**2 + b**2) == c**2
    
    return right_tri




# In[15]:


# STEP2
# Create a new empty list where you will store the dimmensions of all the right triangles

new_list = []


# In[22]:


# STEP3
# Loop over each triangle, determine if its a right triangle 
# using your function, and append to the new list if it is
for triangle in triangles:
    right_tri = check_right_triangle(triangle)
    
    if right_tri:
        print(triangle, "is a right triangle")
        new_list.append(triangle)
    else:
        print(triangle , "not a right triangle")



# In[21]:


print(new_list)


# In[ ]:




