# GWC Color Filters
### GWC SIP Project (Ford 2018)

Using PIL and Python, we can apply any of the following filters to the image "img.png":

(1) The first option (input "1") is "Obamicon". The program applies the maroon-navy-taupe image filter to the given image (much like Obama's "Hope" advertisement). This uses a color threshold to group each pixel by RGB value into maroon, navy or taupe subsets; then each pixel is converted into one of the three colors.

(2) The second option (input "2") is "Grayscale". The program adds the RGB values together and averages them. Each R, G and B value is set to the sum's average.

(3) The third option (input "3) is the "Rainbow Filter". Karli created this filter. The code thresholds pixel location and the sum of the R, G and B values in each pixel to assign each pixel as one of the ROY G BIV colors. This creates a "rainbow" effect across the image while keeping the image itself recognizable.

(4) The fourth option (input "4") is the "Inverse Rainbow". This takes each RGB value for each pixel, and subtracts the value from 255. (For example, a very red pixel with R = 255, G = 0 and B = 0 would have the new value R = 255 - 255 = 0, G = 255 - 0 = 255, B = 255 - 0 = 255). This will give an "inverted" color scheme for each image.

(5) The fifth option (input "5) is the "Sepia Filter". This filter takes the sum's average of the RGB values of each pixel; then it divides this average by three. Decreasing the RGB values like this creates a "faded" effect on the image. Then it increases the R value by 50% and decreaes the B value by 50%. This creates a "yellowing" effect over the image.

If the prompted input is anything other than as suggested above, the program will select a randomized filter to apply to the image.

Results: I learned how to apply PIL and Python to manipulate the RGB values in an image.
