import numpy as np

arr = np.genfromtxt("dataset6.csv",delimiter=",", dtype=str, skip_header=1)
print("Whole Dataset - \n",arr,"\n")

#Converted into float
a = arr[:,1].astype(int)
print("Total Number Of Runs of Each Player -\n",a,"\n") 

#Converted into float
b = arr[:,3].astype(int)
print("Total Number of Balls Played By Each Player -\n",b,"\n") 

#Adding Total Runs and Total Balls
result = np.add(a, b)
print("Sum Of Total Runs and Total Balls -\n",result,"\n")

#Substracting Total Runs and Total Balls
result1 = np.subtract(a, b)
print("Substraction Of Total Runs And Total Balls -\n",result1,"\n")

#Matrix Multiplication of Total Runs and Total Balls
result2 = np.matmul(a, b)
print("Matrix Multiplication Of Total Runs And Total Balls -\n",result2,"\n")

#Transpose Of Total Runs 
result3=np.transpose(a)
print("Transpose of Total Runs -\n",result3,"\n")

#Stack Total Runs and Total Balls Along Rows
result4 = np.hstack((a, b))
print("Stack Along Rows -\n",result4,"\n")

#Stack Total Runs and Total Balls Along Columns
result5= np.vstack((a,b))
print("Stack Along Columns -\n",result5,"\n")

# Generate a Custom Sequence
sequence = np.arange(0,12,1)
print("Customize Range -\n",sequence,"\n")
sequence1=np.linspace(start=0,stop=24,num=12).reshape(3,4)
print("Customize Range with reshape Function -\n",sequence1,"\n")

#Arithmetic and Statistical Operations, Mathematical Operations, Bitwise Operators
multiplication = np.multiply(a,b)
division = np.divide(a,b)
print("Multiplication of Total Runs and Total Balls -\n", multiplication,"\n")
print("Division of Total Runs and Total Balls -\n", division,"\n")

mean = np.mean(a)
median = np.median(a)
std = np.std(a)
var = np.var(a)

print("Mean of Total Runs -\n",mean,"\n")
print("Median of Total Runs -\n",median,"\n")
print("Standard Deviation of Total Runs -\n",std,"\n")
print("Variance of Total Runs -\n",var,"\n")

c=np.bitwise_and(a,b)
print("Bitwise Operator for Total Runs -\n",c,"\n")

e=np.left_shift(a,3)
print("Left Shift For Total Runs -\n",e,"\n")


#Copying Of an Array
c=a.copy()
print("Copied Array of Total Runs -\n",c,"\n")

#View an Array
d=a.view()
a[0]=9854
print("View Array of Total Runs After Changing Runs Of Virat Kohli -\n",d,"\n")

#Searching
maxruns= np.max(a)
minruns = np.min(a)
z= np.where(a > 5000)

#Sorting
sorted_a = np.sort(a)

#Counting
nonzero_count = np.count_nonzero(a)
unique_values, unique_counts = np.unique(a, return_counts=True)

#Broadcasting
arr4 = np.array([1, 2, 3])
arr5 = np.array([[1], [2], [3]])
broadcasted = arr4 + arr5

print("Searching:")
print("Maximum Total Runs -", maxruns)
print("Minimum Total Runs -", minruns)
print("Indices where Total Runs are Greater than 5000 Runs -",z,"\n")

print("Sorting:")
print("Sorted Total Runs Array -", sorted_a,"\n")

print("Counting:")
print("Non-zero Count of Total Runs -", nonzero_count)
print("Unique Values of Total Runs -", unique_values)
print("Unique Counts of Total Runs -", unique_counts,"\n")

print("Broadcasting:")
print("Broadcasted Array -",broadcasted)





