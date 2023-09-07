## Theorem
"Let \( R = 2^n \) for some positive integer \( n \). Consider a circle of radius \( R \) centered at the origin. 
Divide the circle into \( 2R \) equal slices. Then the \( y \)-coordinate of the first slice's intersection point 
above the \( x \)-axis approaches \( \pi \) as \( n \rightarrow \infty \)."

The \(y\)-coordinate of the first slice's intersection point above the \(x\)-axis is given by:

\[
y = R \sin\left(\frac{\pi}{R}\right)
\]

For \( R = 2^n \),

\[
y = 2^n \sin\left(\frac{\pi}{2^n}\right)
\]

We want to find the limit as \(n \to \infty\),

\[
\lim_{{n \to \infty}} 2^n \sin\left(\frac{\pi}{2^n}\right)
\]

We can rewrite \( \sin(x) \) as \( x \) when \( x \) is approaching zero:

\[
\lim_{{n \to \infty}} 2^n \left(\frac{\pi}{2^n}\right) = \lim_{{n \to \infty}} \pi = \pi
\]

Thus, the \( y \)-coordinate approaches \( \pi \) as \( n \rightarrow \infty \).
