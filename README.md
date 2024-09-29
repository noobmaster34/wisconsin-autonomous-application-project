# wisconsin-autonomous-application-project
## This project draws a line following the midpoints in 2 lines of cones

### First attempt: tried defining a broad red color range to detect the cones with openCV. 
#### - pros: 
##### 1. was a simple start to the problem
##### 2. easy solution to debug and learn the basics of OpenCV
##### 3. accurately picked up the red and orange colors of the cones
#### - cons: 
##### 1. was not actually able to show me which items were detected within the colorspace

### Second attempt: researched image thresholding and created a thresholded image of the cones, then displayed the thresholded image. Also realized I was using RGB instead of BRG 
#### - pros: 
##### 1. was able to see what openCV was detecting as red
#### - cons: 
##### 1. The exit sign was detected as a red/orange color
##### 2. The sofa and some parts of the walls were detected as a red/orange color 

### Third attempt: researched common image processing techniques and attempted to use Gaussian blur to simplify the image and reduce the impact of the red exit sign (AKA relevancy - I learned that from the first meeting)
#### - pros:
##### 1. learned something new
#### - cons: 
##### 1. made the problem worse by increasing the noise made by the exit sign 

### Fourth attempt: deleted gaussian blur, narrowed the bgr range 
#### pros: 
##### 1. able to reduce the impact of the exit sign 
#### cons: 
##### 1. still picking up the exit signs

### Fifth attempt: researched more and discovered image contouring, created contours on the images then used integer division to find the centers of the contour. Drew red circles on the midpoints. 
#### pros: 
##### 1. was now ready to draw a line of best fit through the points 
#### cons: 
##### 2. circles were being drawn on the red exit signs 

### Sixth attempt: inserted conditional to determine relevancy of contoured items in the image. set the sweet spot at 50 pixels minimum to be considered significant.
#### pros: 
##### 1. completely eliminated dots from being drawn at the exit signs 
#### cons: 
##### 1. probably a better way to go about relevancy, would not work for an image where there is a red clock for example

### Seventh attempt: drew a line of best fit through the circles using linear regression 
#### cons: 
##### 1. only drew one line through all the points instead of 2 lines 

### Eighth attempt: created a list of points based on x coordinates from left to right and divided the length of the list by 2 to split the points into 2 separate arrays 
#### pros: 
##### 1. now able to draw 2 separate lines 
#### cons: 
##### 1. won't work well with odd numbers (would need to cast the double to an int then I would skip a cone)
##### 2. would work really bad for an image with a small number of cones and an odd number of cones (resulting in a significant reduction in information)
##### 3. would not work for more than 2 lanes of cones



 
