bigimg
======

Easily create big images..

```bigimg.py``` allows you to define a canvas width and height, a vector
function which will conduct an element wise map over each element in the
canvas. If your function returns a single floating point value, the resulting
image will be gray scale, if it returns a 3-tuple, it will be color.


You can also create pseudorandom images with:

```bash
./bigimg 128 128 random pseudorandom.png
```


This is useful in a variety of contexts.

## Examples 

Check out the example images included. You can pull request a new example image
if you find an especially cool formula. Simply add the code to the example set
below, and place the image in the examples/ folder. 


Only the best images, as determined by me, will be accepted.

### Grayscale

```
./bigimg.py 512 512 "lambda x, y: 2048. * np.sin(x/32.) + 2048. * np.sin(y/32.)" examples/1.png
```
![Example 1](examples/1.png "lambda x, y: 2048. * np.sin(x/32.) + 2048. * np.sin(y/32.)" )

```
./bigimg.py 512 512 "lambda x, y: y * np.cos(x/128.)" examples/2.png
```
![Example 2](examples/2.png "lambda x, y: y * np.cos(x/128.)")

### Color

```
./bigimg.py 512 512 "lambda x, y: (x, x, y)" examples/3.png
```
![Example 3](examples/3.png "lambda x, y: (x, x, y)")

```
./bigimg.py 512 512 "lambda x, y: (x, np.sin(x), np.sin(y))" examples/4.png
```
![Example 4](examples/4.png "lambda x, y: (x, np.sin(x), np.sin(y))")

```
./bigimg.py 1024 1024 "lambda x, y: (512 * np.cos(y/32.), 512 * np.sin(x/32.), 512 * np.sin(y/32.))" examples/5.png
```
![Example 5](examples/5.png "lambda x, y: (512 * np.cos(y/32.), 512 * np.sin(x/32.), 512 * np.sin(y/32.))")

