# Recursive Sigma
# Write a recursive function that given a number returns the sum of integers from 1 to that number. Example: rSigma(5) = 15 (1,2,3,4,5);rSigma(2.5) = 3(1+2);rSigma(-1)= 0. 
def rSigma(num):
    if num <= 0:
        return 0
    return num + rSigma(num - 1)

# Recursive Factorial:
# Given num, return the product of ints from 1 up to num. If less than zero, treat as zero. If not an integer, truncate. Experts tell us 0! is 1. rFact(3) = 6(1*2*3). Also, rFact(6.5) = 720 (1*2*3*4*5*6).  
def rFact(num):
    if num <= 0:
        return 1 
    return num * rFact(num - 1)

# Flood Fill
#Most graphical “paint” applications have a ‘paintcan fill’ function that floods part of an image with a certain color. We change the image as if we painted a canvas: a two-dimensional array of integers, where each integer represents a color for that pixel. The canvas Array.length is the Y dimension of our canvas; each spot in the canvas array is a row in our image, with a length equal to our canvas’ X dimension. You are given a canvas (2-dimensional array of integers), starting coordinate (2-element array), and the color to flood (integer value). Build floodFill(canvas2D,startXY,newColor)! Replace a pixel’s color value only if it is the same color as the origin coordinate and is directly adjacent via X or Y to another pixel you will change. 

# Note: diagonally related pixels are not considered adjacent.
def flood_fill(canvas, startXY, new_color):
    def fill(x, y):
        if x < 0 or x >= len(canvas) or y < 0 or y >= len(canvas[0]) or canvas[x][y] != start_color:
            return
        canvas[x][y] = new_color
        fill(x + 1, y)
        fill(x - 1, y)
        fill(x, y + 1)
        fill(x, y - 1)

    start_color = canvas[startXY[0]][startXY[1]]
    if start_color == new_color:
        return canvas

    fill(startXY[0], startXY[1])
    return canvas

print(rSigma(5))
print(rSigma(2.5))
print(rSigma(-1))

print(rFact(3))
print(rFact(6.5))

canvas = [
    [1,1,1,1,1],
    [1,1,3,3,1],
    [1,1,3,3,3],
    [1,1,1,1,3]
]

startXY = [2,2]
new_color = 2

result = flood_fill(canvas, startXY, new_color)

for row in result:
    print(row)