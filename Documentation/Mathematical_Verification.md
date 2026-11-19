# Mathematical Verification

Given:

\[
f(x,y)=x^2+2y^2.
\]

Partial derivatives:

\[
f_x=2x,\qquad f_y=4y.
\]

Gradient:

\[
\nabla f(x,y)=(2x,4y).
\]

At \(P=(1,1)\):

\[
\nabla f(1,1)=(2,4).
\]

Magnitude:

\[
\|\nabla f(1,1)\|=\sqrt{2^2+4^2}=\sqrt{20}=2\sqrt5.
\]

Unit direction of steepest increase:

\[
\frac{(2,4)}{2\sqrt5}=\left(\frac1{\sqrt5},\frac2{\sqrt5}\right).
\]

For a unit vector \(u\), the directional derivative is:

\[
D_uf=\nabla f\cdot u=\|\nabla f\|\cos\theta.
\]

Because \(\cos\theta\leq1\), the maximum occurs at \(\theta=0\), when \(u\) points in the direction of the gradient. The maximum rate is therefore \(2\sqrt5\) at \(P=(1,1)\).

A regular level curve has constant function value. Differentiating \(f(r(t))=c\) gives \(\nabla f(r(t))\cdot r'(t)=0\), so the gradient is normal to the level curve when it is nonzero.
