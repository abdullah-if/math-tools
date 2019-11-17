# math-tools
A set of general purpose mathmetical tools
The tools are available both in interactive and direct from environment format. All codes are well commented and easy to understand for beginers.Codes are written in Python 3, C and FORTRAN.
R is coming soon.

For getting the tools, use this command line

`git clone https://www.github.com/Nemo-Nowane/math-tools`

**Note:The one with *-ia* are interactive.**

For directly accessing from CLI with ease,
Run these once:
```
#crontab -e
@reboot  ~/math-tools/sources/alias.sh
```


## Quadratic Solver 
The code needs the coefficients of the equation as input.

## Table maker
Able to make table of any polynomial function of single variable. 
Requires the coefficients of the variable in desending order, starting point, ending point and step deviation respectively, as input.

## Equation solver
Takes coefficients as input. Solves polynomial of single variable. Uses following algorithm:
According to factor theorem,
if P(x)= aₙxⁿ + aₙ₋₁xⁿ⁻¹+......... +a₀

then solutions of P(x) can expressed as p/q when p is a factor of a₀  and q is a factor of aₙ while aₙ and a₀ are integers. Here p and q may be positive or negative.
Since, qx-p is factor of the polynomial. For more decent explanation visit [Wikipedia] (https://en.m.wikipedia.org/wiki/Factorization_of_polynomials#Classical_methods#Obteining_linear_factor) 
 
This site was built using [GitHub Pages](https://pages.github.com/).

*Note: The programme turns non-integer coefficients in integer in runtime.*

*P.S.:If the a₀ is missing then 0 is a solution for the function. This is also considered in the programme.*

## Wide range trigonometric calculator
A legacy code. It was my first self-made algorithm. Runs well. **Only interactive format available.**
Compiling it in CLI, use following command :
`gcc  WRTC.c -lm -o WRTC`

(clang if you have that instesd of gcc)
