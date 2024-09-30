#list of squares
squares = []
for number in range(1, 11):
    square = number**2
    squares.append(square)

#sum of the squares    
sum = 0
for square in squares:
    sum += square

#print mininimum, maximum and sum
print("minimum: " + str(squares[0]) +
    "\nmaximum: " + str(squares[9]) +
    "\nsum: " + str(sum)
    )
