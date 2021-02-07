
### Welcome to Statistical inference case study.
- In this case study you are given a set of questions which needs to be answered using your knowledge on statistics.
- For each question assign your answers to respective variables in the following cells.
- Create a new notebook (will not be graded to try out your scripts ans assign the 
- All the answers are expected to be rounded off to two decimal places.
- Once you assign your answers to variables in each cell run the cell to display incorrect answers if any.
- Dont leave any variables unassigned.
- Dont edit the script ment for evaluation
- Once you are done with your solutions run all the cells (kernel -> Restart & run all).

import numpy as np
import math
import scipy.stats as st

import dill

Quiz = dill.load(open("QuizClass.pik", 'rb'))
quiz = dill.load(open('Quiz.pik', 'rb'))

1. Suppose a variable X has a bell-shaped distribution with a mean of 150 and a standard deviation of 20.  
a. What percentage of X values lies between 130 and 170?  
b. What percentage of X values lies between 110 and 190?  
c. What percentage of X values lies above 190?  

### Assign your answers here
a = 1 - (st.norm.cdf(130,150,20))*2
b = 1 - (st.norm.cdf(110,150,20))*2
c = 1 - (st.norm.cdf(190,150,20))


a_1 = int(round(a,2)*100)
b_1 = int(round(b,2)*100)
c_1 = round(c*100,2)

### For evalution
ans_1 = {"a_1":math.floor(a_1), "b_1": b_1, "c_1" : c_1}
quiz.eval(1, ans_1)


2. Variable X has a mean of 15 and a standard deviation of 2.  
    a. What percentage of X values will lie within 1.5 standard deviation of the mean?     
    b. What is the minimum percentage of X values that lie between 8 and 17?  

### Assign your answers here
normal_dist = scipy.stats.norm(15, 2)
a_2 = round((normal_dist.cdf(18) - normal_dist.cdf(12))*100, 2)
b_2 = round((normal_dist.cdf(17) - normal_dist.cdf(8))*100, 2)

### For evalution
ans_2 = {"a_2":a_2, "b_2": b_2}
quiz.eval(2, ans_2)

3. What is the 25 percentile of the below samples  
   [3.09, 2.48, 2.02, 2.98, 3.53, 2.41, 2.01, 2.95, 2.63, 3.09, 3.26,
   2.04, 3.74, 2.99, 2.34, 2.77, 3.05, 3.29, 3.14, 3.17]
        

### Assign your answers here
arr = [3.09, 2.48, 2.02, 2.98, 3.53, 2.41, 2.01, 2.95, 2.63, 3.09, 3.26, 2.04, 3.74, 2.99, 2.34, 2.77, 3.05, 3.29, 3.14, 3.17]
a_3 = round(np.percentile(arr, 25),2)

###For evaluation
ans_3 = {"a_3": a_3}
print(ans_3)
quiz.eval(3, ans_3)

4. Suppose a marble is randomly selected from a jar containing 12 red, 4 black, and 8 blue marbles. Find the   probability of the following:  
a. The marble is red or black  
b. The marble is black or blue  
c. The marble is not blue  
d. The marble is red or not blue  

### Assign your answers here
t = 12 + 4 + 8
a_4 = round((12+4)/t, 2)
b_4 = round((4+8)/t, 2)
c_4 = round((12+4)/t, 2)
d_4 = round((12+4)/t, 2)

#######OR##############
from scipy.special import comb
a_4 = round(comb(12+4, 1) / comb(24, 1), 2)
b_4 = round(comb(8+4, 1) / comb(24, 1), 2)
c_4 = a_4
d_4 = a_4
### For evalution
ans_4 = {"a_4":a_4, "b_4": b_4, "c_4" : c_4, "d_4": d_4}
quiz.eval(4, ans_4)

5. Let A and B be events with P(A) = 0.2, P(B) = 0.8, and P(A ∩ B) = 0.1 Find the following  
   a. $P(\bar B)$  
   b. $P(\bar A \cap \bar B)$  
   c. $P(\bar B \space | \space A)$   
   d. $P(\bar A \cap B)$  

### Assign your answers here
au = 0.2 + 0.8 - 0.1
a_5 = round((1 - 0.8),2)
b_5 = round((1 - au),2)
c_5 = round(((0.2 -0.1)/0.2),2)
d_5 = round((0.8 - 0.1),2)

### For evalution
ans_5 = {"a_5":a_5, "b_5": b_5, "c_5" : c_5, "d_5": d_5}

quiz.eval(5, ans_5)

6. Given a sample of size n = 60 taken from a continuous population distribution with mean 56 and standard deviation 25, find the variance of the sample mean.

### Assign your answers here
variance = round(((25**2)/60),2)

### For evalution
ans_6 = {"variance": variance}
quiz.eval(6, ans_6)

7. 55% of all engineering students prefer internship over final year project. Suppose 12 students are randomly selected and the number in favor of internship is recorded. Find the following:  
a. The probability that exactly seven of them choose internship.  
b. The probability that at most eight of them choose internship.  
c. The probability that at least five of them choose internship.  
d. The probability that at least seven, but no more than 10, choose internship.  

### Assign your answers here
from math import factorial

def calculate_combinations(n, r):
    return factorial(n) // factorial(r) // factorial(n-r)

a_7 = round(calculate_combinations(12, 7)*(0.55**7)*(0.45**5),2)

p9 = calculate_combinations(12, 9)*(0.55**9)*(0.45**3)
p10 = calculate_combinations(12, 10)*(0.55**10)*(0.45**2)
p11 = calculate_combinations(12, 11)*(0.55**11)*(0.45**1)
p12 = calculate_combinations(12, 12)*(0.55**12)*(0.45**0)

b_7 = round(1 - (p9 + p10 + p11 + p12),2)

p0 = calculate_combinations(12, 0)*(0.55**0)*(0.45**12)
p1 = calculate_combinations(12, 1)*(0.55**1)*(0.45**11)
p2 = calculate_combinations(12, 2)*(0.55**2)*(0.45**10)
p3 = calculate_combinations(12, 3)*(0.55**3)*(0.45**9)
p4 = calculate_combinations(12, 4)*(0.55**4)*(0.45**8)

c_7 = round(1-(p0+p1+p2+p3+p4),2)

p7 = calculate_combinations(12, 7)*(0.55**7)*(0.45**5)
p8 = calculate_combinations(12, 8)*(0.55**8)*(0.45**4)
p9 = calculate_combinations(12, 9)*(0.55**9)*(0.45**3)
p10 = calculate_combinations(12, 10)*(0.55**10)*(0.45**2)

d_7 = round(p7+p8+p9+p10 ,2)
############OR############
binom_dist = scipy.stats.binom(12, 0.55)
a_7 = round(binom_dist.pmf(7), 2)
b_7 = round(binom_dist.cdf(8), 2)
c_7 = round(binom_dist.sf(4), 2)
d_7 = round(binom_dist.sf(6) - binom_dist.sf(10), 2)

### For evalution
ans_7 = {"a_7":a_7, "b_7": b_7, "c_7" : c_7, "d_7": d_7}

quiz.eval(7, ans_7)

8. Suppose the population variable X is N(3, 0.3) and n = 20. How large an interval must be chosen so that the probability is 0.95 that the sample mean $\bar X$ lies within ±a units of the population mean μ?

### Assign your answers here
interval = 0.4

### For evalution
ans_8 = {"interval":np.around(interval, 1)}
quiz.eval(8, ans_8)

9. A random variable X is N(25, 4). Find the indicated percentile for X:  
a. The 10th percentile   
b. The 90th percentile  
c. The 80th percentile  
d. The 50th percentile  

### Assign your answers here
# The answers doesn't exactly matches the test_answers. 
# The answers present in comments are the actual answers.
dist = scipy.stats.norm(25, 4)
a_9 = round(dist.ppf(0.10), 2)  # 19.88
b_9 = round(dist.ppf(0.90), 2)  # 30.12
c_9 = round(dist.ppf(0.80), 2)  # 28.36
d_9 = round(dist.ppf(0.50), 2)

### For evalution
ans_9 = {"a_9":a_9, "b_9": b_9, "c_9" : c_9, "d_9": d_9}
quiz.eval(9, ans_9)

### Run the below cell to save your answers for final evaluation

with open('Quiz.pik', 'wb') as file:
    dill.dump(quiz, file)
quiz = dill.load(open('Quiz.pik', 'rb'))
quiz.score()

