from parametric import TWMSolver as TWM, a_p, a_s, PF
from sympy.physics.quantum.boson import BosonOp
from sympy.core.sympify import sympify
from sympy.core.singleton import S
from sympy.core.symbol import symbols, Symbol, Dummy
from sympy.core.add import Add
from sympy.core.mul import Mul
from sympy.core.power import Pow
from sympy.functions.elementary.trigonometric import cos, sin 
from sympy.functions.elementary.hyperbolic import cosh, sinh

pf1 = PF({((), ()): S.One})
s = TWM(False)
print(s.to_expr(s.bdswap(a_s.adjoint(), {(0, 1, 1): pf1})))
        # elif isinstance(expr, Sum):
        #     v = (l[0] for l in expr.limits)
        #     ff, fo = self.leading_order(expr.function)
        #     inc = set(v) & fo.atoms()
        #     if inc:
        #         from sympy.polys.polytools import Poly
        #         from sympy.polys.polyerrors import PolynomialError
        #         try:
        #             po = Poly(fo.expand(), *v)
        #             if po.total_degree() <= 1:
        #                 subs = dict()
        #                 for l in expr.limits:
        #                     if l[0] in inc:
        #                         c = po.coeff_monomial(l[0])
        #                         if c.is_positive:
        #                             subs[l[0]] = l[1]
        #                         elif c.is_negative:
        #                             subs[l[0]] = l[2]
        #                         else:
        #                             raise ValueError('Unable to determine the leading order')
        #                 exhaust = False
        #             else:
        #                 exhaust = True
        #         except PolynomialError:
        #             exhaust = True
        #         if exhaust:
        #             vars = []
        #             bases = []
        #             sizes = []

        #             for v, ll, ul in expr.limits:
        #                 if v in inc:
        #                     d = ul - ll
        #                     if not (d.is_Integer and d.is_nonnegative):
        #                         raise ValueError('Unable to determine the leading order')
        #                     vars.append(v)
        #                     bases.append(ll)
        #                     sizes.append(d)
        #             m = S.Infinity
        #             terms = []
        #             from itertools import product
        #             for idx in product(*(range(s) for s in sizes)):
        #                 subs = {v: b + i for v, b, i in zip(vars, bases, idx)}
        #                 subexpr = ff.subs(subs)
        #                 o = fo.subs(subs)
        #                 if m == o:
        #                     terms.append(subexpr)
        #                 else:
        #                     cond = m is S.Infinity or m > o
        #                     if isinstance(cond, Relational):
        #                         raise ValueError('Unable to determine the leading order')
        #                     if cond:
        #                         m = o
        #                         terms = [subexpr]
        #             if len(inc) == len(expr.limits):
        #                 t = Add(*terms)
        #             else:
        #                 ol = (l for l in expr.limits if l[0] not in inc)
        #                 t = Sum(Add(*terms), *ol)
        #         else:
        #             if len(inc) == len(expr.limits):
        #                 t = ff.subs(subs)
        #             else:
        #                 ol = (l for l in expr.limits if l[0] not in inc)
        #                 t = Sum(ff.subs(subs), *ol)
        #             m = fo.subs(subs)
        #     else:
        #         t, m = ff, fo

        # elif isinstance(expr, Sum):
        #     fo = self.leading_order(expr.function)[1]
        #     if (fo > n) == False:
        #         for t, o in self.expand_upto(expr.function, n):
        #             yield Sum(t, expr.limits), o
        #     else:
        #         warnings.warn('Expect the order to be independent of sum indices')
        #         yield from ()
