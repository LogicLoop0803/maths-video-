# Viva Preparation — Gradient: Direction of Steepest Increase

## 1. What is a gradient?
For a differentiable scalar function of two variables, the gradient is the vector of its first partial derivatives: ∇f=(∂f/∂x, ∂f/∂y). It describes the direction and rate of the greatest local increase.

## 2. What does a partial derivative mean?
∂f/∂x measures the instantaneous change in f as x changes while y is held constant. ∂f/∂y does the same while y changes and x is held constant.

## 3. Find the gradient of f(x,y)=x²+2y².
Differentiate with respect to x: fₓ=2x. Differentiate with respect to y: fᵧ=4y. Therefore ∇f=(2x,4y).

## 4. Evaluate it at P=(1,1).
∇f(1,1)=(2,4).

## 5. Find its magnitude.
||∇f(1,1)||=√(2²+4²)=√20=2√5. This is the maximum directional derivative at that point.

## 6. Find the unit vector of steepest increase.
Divide the gradient by its magnitude: (2,4)/(2√5)=(1/√5,2/√5).

## 7. Why is the gradient the steepest direction?
For any unit direction u, Dᵤf=∇f·u=||∇f||cosθ. Since cosθ≤1, the largest value occurs at θ=0, when u points in the same direction as the gradient.

## 8. Why is the gradient perpendicular to a level curve?
Along a differentiable level curve r(t), f(r(t))=c is constant. Differentiating gives ∇f(r(t))·r′(t)=0. Thus, when the gradient is nonzero, it is perpendicular to the tangent of the level curve.

## 9. Is the steepest direction global or local?
It is local. The gradient gives the direction of greatest instantaneous increase at the current point; it does not guarantee the best long-distance route.

## 10. What if the gradient is zero?
All first-order directional derivatives are zero at that point. The gradient does not identify a unique steepest direction there; higher-order analysis may be needed.

## 11. What does the gradient magnitude tell us?
It equals the maximum directional derivative, so it gives the maximum instantaneous rate of increase per unit distance at the point.

## 12. Explain the code.
The visual renderer creates frames with mathematical labels, contours and vectors, writes frames to an MP4, and FFmpeg can retime and combine the visual sequence with the narration.

## 13. Why use f(x,y)=x²+2y²?
It is simple to differentiate, has elliptical level curves, and gives a nonzero gradient at P=(1,1), making the steepest direction and perpendicularity easy to demonstrate.

## 14. What AI tools were used?
AI assistance was used for planning, code and documentation support. HeyGen Voice generated the Indian-English male narration. The mathematical example and derivation are documented for independent explanation.
