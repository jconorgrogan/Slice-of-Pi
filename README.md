##  Slice of Pi 
TLDR; Geomtric way of representing a derivation of Viete's formula for pi that involves nested square roots of two

### Definitions and Assumptions

Let \( R = 2^n \) for some positive integer \( n \). Consider a circle of radius \( R \) centered at the origin. Divide the circle into \( 2R \) equal slices. The \( y \)-coordinate of the first slice's intersection point above the \( x \)-axis approaches \( \pi \) as \( n \rightarrow \infty \).

1. Define \( R = 2^n \) where \( n \) is a positive integer.
    - ![R = 2^n](https://latex.codecogs.com/gif.latex?R%20%3D%202%5En)
2. Consider a circle of radius \( R \) centered at the origin.
3. Divide the circle into \( 2R \) equal slices.
4. The angle for each slice is \( \theta = \frac{2\pi}{2R} = \frac{\pi}{R} \).
    - ![theta](https://latex.codecogs.com/gif.latex?%5Ctheta%20%3D%20%5Cfrac%7B2%5Cpi%7D%7B2R%7D%20%3D%20%5Cfrac%7B%5Cpi%7D%7BR%7D)

### Y-Coordinate Expression
The \( y \)-coordinate for the first slice's intersection point above the \( x \)-axis in Cartesian coordinates is \( y = R \sin(\theta) \). Substituting \( \theta = \frac{\pi}{R} \) and \( R = 2^n \), we get \( y = 2^n \sin\left(\frac{\pi}{2^n}\right) \).
    - ![y-coordinate expression](https://latex.codecogs.com/gif.latex?y%20%3D%202%5En%20%5Csin%5Cleft%28%5Cfrac%7B%5Cpi%7D%7B2%5En%7D%5Cright%29)

### Limit Calculation
We want to find \( \lim_{n \to \infty} 2^n \sin\left(\frac{\pi}{2^n}\right) \).
    - ![limit calculation](https://latex.codecogs.com/gif.latex?%5Clim_%7Bn%20%5Cto%20%5Cinfty%7D%202%5En%20%5Csin%5Cleft%28%5Cfrac%7B%5Cpi%7D%7B2%5En%7D%5Cright%29)

Substitute \( u = \frac{\pi}{2^n} \) and \( 2^n = \frac{\pi}{u} \), so \( u \to 0 \) as \( n \to \infty \).
The limit becomes \( \lim_{u \to 0} \frac{\pi}{u} \sin(u) \).
Utilizing the limit identity \( \lim_{u \to 0} \frac{\sin(u)}{u} = 1 \), the limit is \( \pi \).
    - ![limit result](https://latex.codecogs.com/gif.latex?%5Clim_%7Bu%20%5Cto%200%7D%20%5Cfrac%7B%5Cpi%7D%7Bu%7D%20%5Csin%28u%29%20%3D%20%5Cpi)

**Conclusion**:
- Therefore, the \( y \)-coordinate of the first slice's intersection point above the \( x \)-axis approaches \( \pi \) as \( n \rightarrow \infty \).

## Generalized Slice of Pi Theorem for k-th Intersection Point

### Theorem
Let \( R = 2^n \) for some positive integer \( n \). Consider a circle of radius \( R \) centered at the origin and divide it into \( 2R \) equal slices. The \( y \)-coordinate of the \( k \)-th slice's intersection point above the \( x \)-axis approaches \( k\pi \) as \( n \rightarrow \infty \).

### Definitions and Assumptions
- Define \( R = 2^n \) where \( n \) is a positive integer.
- Consider a circle of radius \( R \) centered at the origin.
- Divide the circle into \( 2R \) equal slices.
- The angle for the \( k \)-th slice is \( \theta_k = k \left( \frac{2\pi}{2R} \right) = k \left( \frac{\pi}{R} \right) \).

### Y-Coordinate Expression
The \( y \)-coordinate for the \( k \)-th slice's intersection point above the \( x \)-axis in Cartesian coordinates is \( y_k = R \sin(\theta_k) \).

Substituting \( \theta_k = k \frac{\pi}{R} \) and \( R = 2^n \), we get:
\[ y_k = 2^n \sin\left(k \frac{\pi}{2^n}\right) \]

### Limit Calculation
We want to find \( \lim_{n \to \infty} 2^n \sin\left(k \frac{\pi}{2^n}\right) \).

Substitute \( u = k \frac{\pi}{2^n} \) and \( 2^n = \frac{k \pi}{u} \), so \( u \to 0 \) as \( n \to \infty \).

The limit becomes \( \lim_{u \to 0} \frac{k \pi}{u} \sin(u) \).

Utilizing the limit identity \( \lim_{u \to 0} \frac{\sin(u)}{u} = 1 \), the limit is \( k \pi \).

Therefore, as \( n \rightarrow \infty \), the \( y \)-coordinate of the \( k \)-th intersection point will approach \( k \pi \).

5. **Conceptual framing**

Infinite Equally-Spaced Elements:
Imagine an infinite one-dimensional line with equally spaced points or elements. Each element is indistinguishable in itself; what matters is the uniform spacing (the relationships) between them.
Now, consider an external observer who is not part of that infinite line. This observer perceives the pattern of spacing and can reinterpret those infinite, uniform relationships as forming a circle. The circle arises because the external perspective "wraps" the infinite line into a finite, cyclic structure.
Within this circle, when you focus on the smallest possible difference between adjacent elements (or slices), you find that—when scaled in the context of the whole—the cumulative effect of all these minimal differences amounts to 
2π. In other words, from the perspective of the entire structure (the sum of all these relationships),
2π represents the complete, finite measure (the full angular cycle of the circle).
Thus, from this lens, 

2π encapsulates the sum of all the smallest possible relationships, viewed as a whole. It’s as if the entire structure, which "has everything in common," manifests itself in the form of a circle whose total measure (or circumference in the unit radius case) is 

2π.

8. **Visualizations**:


![image](https://github.com/jconorgrogan/Grogans-Slice-of-Pi/assets/130090573/bed128bf-b7ac-45d1-9fc7-805c611892bd)

Each of these horizontal lines approaches a multiple of pi as R goes to infinity
![image](https://github.com/jconorgrogan/Grogans-Slice-of-Pi/assets/130090573/2a204d04-0238-44ed-a5f4-a91fe5c68617)


As R increases, each 2nd node y coordinate moves towards 2pi, 3rd node 3pi, etc. 
How each point converges to these multiples of pi creates some extremely interesting fractals which are worthy of future research

The infinite prime ladder, and the Grogan Rollercoaster 
![image](https://github.com/jconorgrogan/Grogans-Slice-of-Pi/assets/130090573/f45b1293-16f1-41fd-abdf-ead3df0f4284)

