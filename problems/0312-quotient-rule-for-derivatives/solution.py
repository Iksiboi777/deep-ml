import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """

    def poly_derive(coeffs, x):
        cz = []
        n = len(coeffs) - 1

        for c in coeffs[:-1]:           
            cz.append(c*n*(x**(n-1)))
            n -= 1
        return sum(cz)

    g_der = poly_derive(g_coeffs, x)
    print("G_der: ", g_der)
    h_der = poly_derive(h_coeffs, x)
    print("H_der: ", h_der)

    g = sum([c*x**i for i, c in enumerate(reversed(g_coeffs))])
    print("G: ", g)
    h = sum([c*x**i for i, c in enumerate(reversed(h_coeffs))])
    print("H: ", h)
    
    return (g_der*h - g*h_der)/(h**2)