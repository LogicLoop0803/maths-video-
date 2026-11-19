# Narration Script — Gradient: Direction of Steepest Increase

**Target duration:** 4 minutes 15 seconds (generated narration: 255.27 seconds)  
**Voice:** Indian-English male voice  
**Student:** Mohammad Mustafa  
**Student ID:** E25B070875

## Scene 1 — Hook and context (0:00–0:29)

Imagine standing on a hill. You can walk in many directions. Some directions take you uphill quickly, while others barely change your height. If the hill is represented by a function of two variables, how can we identify the direction that increases the height most rapidly? This question leads us to a powerful idea in multivariable calculus: the gradient. By the end of this video, you will know how to calculate it and why it points toward the steepest local increase.

## Scene 2 — Concept introduction (0:29–1:09)

A function of two variables, written as f of x comma y, takes an input pair, x and y, and returns one number. We can imagine that number as height. The gradient is a vector containing the two partial derivatives. We write it as nabla f, and it equals the partial derivative with respect to x, followed by the partial derivative with respect to y. The first partial derivative measures how the output changes when x changes and y is held fixed. The second measures how the output changes when y changes and x is held fixed. Together, these two values describe the local change in both coordinate directions.

## Scene 3 — Visual intuition (1:09–1:46)

Before calculating, look at this contour map. Each contour joins points with the same function value, just like elevation lines on a real topographic map. If you walk along one contour, your height does not change. At a regular point, the gradient is perpendicular to the contour passing through that point. It points across the contours toward larger values. Notice that this is a local statement: the gradient tells us the best direction for an immediate step, not necessarily the best long-distance route across an entire landscape. The length of the gradient tells us the maximum rate of increase at that point.

## Scene 4 — Worked example (1:46–2:41)

Let us use a simple function: f of x comma y equals x squared plus two y squared. First, calculate the partial derivative with respect to x. While differentiating with respect to x, treat y as a constant. The derivative of x squared is two x, and the derivative of two y squared is zero. So f sub x equals two x. Next, differentiate with respect to y, treating x as a constant. The derivative of x squared is zero, and the derivative of two y squared is four y. So f sub y equals four y. Therefore, the gradient is the vector two x comma four y. Now consider the point P equals one comma one. Substituting these coordinates gives the gradient two comma four. Its magnitude is the square root of two squared plus four squared. That is the square root of twenty, which simplifies to two root five.

## Scene 5 — Why it is the steepest direction (2:41–3:44)

Now let us prove why this vector gives the steepest direction. Choose any unit direction vector, called u. A unit vector has length one. The directional derivative, which measures the instantaneous rate of change in that direction, is the dot product of the gradient and u. The dot product can also be written as the magnitude of the gradient, multiplied by the magnitude of u, and multiplied by cosine theta, where theta is the angle between the two vectors. Since u is a unit vector, its magnitude is one. So the directional derivative equals the magnitude of the gradient times cosine theta. The largest possible value of cosine theta is one, and that happens when theta is zero degrees. In other words, u points in exactly the same direction as the gradient. Therefore, the gradient gives the direction of steepest local increase, and its magnitude gives the maximum rate. At our point, the maximum rate is two root five. The corresponding unit direction is one over root five, comma, two over root five.

## Scene 6 — Summary and credits (3:44–4:15)

Let us remember three key ideas. First, the gradient is formed by collecting the partial derivatives. Second, at a regular point, it is perpendicular to the level curve. Third, it points in the direction of greatest instantaneous increase, and its magnitude is that maximum rate. We used the function x squared plus two y squared to calculate and interpret a real gradient. Thank you for watching. This project was prepared with AI assistance. The mathematical derivation and numerical example are included in the repository for review.

## Pronunciation notes

- Gradient: GRAY-dee-uhnt
- Nabla: NAB-luh
- Read ∇f as “the gradient of f”.
- Read D sub u f as “the directional derivative of f in direction u”.
