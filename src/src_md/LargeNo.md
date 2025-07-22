# Laws of Large Numbers

Chebyshev’s Inequality: Let $X$ be a random variable and $a \in \mathbb { R } ^ { + }$ . We assume $X$ has density function $f _ { X }$ . Then

$$
\begin{array} { r c l } { E ( X ^ { 2 } ) } & { = } & { \displaystyle \int _ { \mathbb R } x ^ { 2 } f _ { X } ( x ) d x } \\ & { \geq } & { \displaystyle \int _ { | x | \geq a } x ^ { 2 } f _ { X } ( x ) d x } \\ & { \geq } & { a ^ { 2 } \displaystyle \int _ { | x | \geq a } f _ { X } ( x ) d x = a ^ { 2 } \mathrm { P } \left( | X | \geq a \right) . } \end{array}
$$

That is, we have proved

$$
\operatorname { P } \left( | X | \geq a \right) \leq { \frac { 1 } { a ^ { 2 } } } E ( X ^ { 2 } ) .
$$

We can generalize this to any moment $p > 0$ :

$$
\begin{array} { l l l } { E ( | X | ^ { p } ) } & { = } & { \displaystyle \int _ { \mathbb R } | x | ^ { p } f _ { X } ( x ) d x } \\ & { \geq } & { \displaystyle \int _ { | x | \geq a } | x | ^ { p } f _ { X } ( x ) d x } \\ & { \geq } & { a ^ { p } \displaystyle \int _ { | x | \geq a } f _ { X } ( x ) d x = a ^ { p } \mathrm { P } \left( | X | \geq a \right) . } \end{array}
$$

That is, we have proved

$$
\operatorname { P } \left( | X | \geq a \right) \leq { \frac { 1 } { a ^ { p } } } E ( | X | ^ { p } )
$$

for any $p = 1 , 2 , \ldots$ (Of course, this assumes that $E ( | X | ^ { p } ) < \infty$ for otherwise the inequality would not be saying much!)

Remark: We have proved (1) and (2) assuming $X$ has a density function $f _ { X }$ . However, (almost) identical proofs show the same inequalities for $X$ having a discrete distribution.

Weak Law of Large Numbers: Let $X _ { 1 }$ , $X _ { 2 } , X _ { 3 }$ , . . . be a sequence of independent random variables with common distribution function. Set $\mu = E ( X _ { j } )$ and $\sigma ^ { 2 } = \operatorname { V a r } ( X _ { j } )$ . As usual we define

$$
S _ { n } = X _ { 1 } + X _ { 2 } + \cdot \cdot \cdot + X _ { n }
$$

and let

$$
S _ { n } ^ { * } = { \frac { S _ { n } } { n } } - \mu .
$$

We apply Chebyshev’s inequality to the random variable $S _ { n } ^ { * }$ . A by now routine calculation gives

$$
E ( S _ { n } ^ { * } ) = 0 { \mathrm { ~ a n d ~ } } \operatorname { V a r } ( S _ { n } ^ { * } ) = { \frac { \sigma ^ { 2 } } { n } } .
$$

Then Chebyshev (1) says that for every $\varepsilon > 0$

$$
\operatorname { P } \left( | S _ { n } ^ { * } | \geq \varepsilon \right) \leq { \frac { 1 } { \varepsilon ^ { 2 } } } \operatorname { V a r } ( S _ { n } ^ { * } ) .
$$

Writing this out explicitly:

$$
\mathrm { P } \left( \left| { \frac { X _ { 1 } + X _ { 2 } + \cdots + X _ { n } } { n } } - \mu \right| \geq \varepsilon \right) \leq { \frac { 1 } { \varepsilon ^ { 2 } } } { \frac { \sigma ^ { 2 } } { n } } .
$$

Thus for every $\varepsilon > 0$ , as $n \to \infty$

$$
\operatorname { P } ( | { \frac { X _ { 1 } + X _ { 2 } + \cdots + X _ { n } } { n } } - \mu | \geq \varepsilon )  0 .
$$

Borel-Cantelli Lemma: Let $A _ { 1 }$ , $A _ { 2 } , \ldots$ be an infinite sequence of events in $\Omega$ . Consider the sequence of events

$$
\bigcup _ { n = 1 } ^ { \infty } A _ { n } , \bigcup _ { n = 2 } ^ { \infty } A _ { n } , \bigcup _ { n = 3 } ^ { \infty } A _ { n } , \ldots .
$$

Observe that this is a decreasing sequence in the sense that

$$
\bigcup _ { n = m + 1 } ^ { \infty } A _ { n } \subseteq \bigcup _ { n = m } ^ { \infty } A _ { n }
$$

for all $m = 1 , 2 , \ldots$ . We are interested in those events $\omega$ that lie in infinitely many $A _ { n }$ . Such $\omega$ would lie in $\textstyle \bigcup _ { m = n } ^ { \infty }$ for every $m$ . Thus we define

$$
\operatorname* { l i m s u p } _ { m = \infty } \operatorname* { l i m } _ { m \to \infty } \bigcup _ { n = m } ^ { \infty } A _ { n } = \left\{ \omega \operatorname { t h a t } { \mathrm { ~ a r e ~ i n ~ i n f i n i t e l y ~ m a n y ~ } } A _ { n } \right\} .
$$

We write this event as

$$
\operatorname* { l i m s u p } A _ { n } = \{ \omega \in A _ { n } { \mathrm { i . o . } } \}
$$

where “i.o.” is read as “infinitely often.” We can now state the BorelCantelli Lemma:

If $\textstyle \sum _ { n = 1 } ^ { \infty } \operatorname { P } ( A _ { n } ) < \infty$ , then $\operatorname { P } \left( \omega \in A _ { n } { \mathrm { i . o . } } \right) = 0$ .

Proof: First observe that

$$
0 \leq \operatorname* { l i m s u p } A _ { n } \subseteq \bigcup _ { m = n } ^ { \infty } A _ { n }
$$

for every $m$ since the sequence is a decreasing sequence of events. Thus

$$
0 \leq \mathrm { P } \left( \operatorname* { l i m s u p } A _ { n } \right) \leq \sum _ { n = m } ^ { \infty } \mathrm { P } ( A _ { n } )
$$

for every $m$ . But we are assuming that the series $\textstyle \sum _ { n = 1 } ^ { \infty } \operatorname { P } ( A _ { n } )$ converges. This means that

$$
\sum _ { n = m } ^ { \infty } \operatorname { P } ( A _ { n } ) \to 0 { \mathrm { ~ a s ~ } } m \to \infty .
$$

Taking $m \to \infty$ in (3) then gives (since the right hand side tends to zero)

$$
\mathrm { P } ( \operatorname* { l i m s u p } A _ { n } ) = 0 .
$$

Strong Law of Large Numbers: As above, let $X _ { 1 }$ , $X _ { 2 }$ , $X _ { 3 } \ldots$ denote an infinite sequence of independent random variables with common distribution. Set

$$
S _ { n } = X _ { 1 } + \cdot \cdot \cdot + X _ { n } .
$$

Let $\mu = E ( X _ { j } )$ and $\sigma ^ { 2 } = \operatorname { V a r } ( X _ { j } )$ . The weak law of large numbers says that for every sufficiently large fixed $n$ the average $S _ { n } / n$ is likely to be near $\mu$ . The strong law of large numbers ask the question in what sense can we say

$$
\operatorname* { l i m } _ { n \to \infty } { \frac { S _ { n } ( \omega ) } { n } } = \mu .
$$

Clearly, (4) cannot be true for all $\omega \in \Omega$ . (Take, for instance, in coining tossing the elementary event $\omega = H H H H . .$ . for which $S _ { n } ( \omega ) = 1$ for every $n$ and hence $\operatorname* { l i m } _ { n \to \infty } S _ { n } ( \omega ) / n = 1$ .) Thus we want to look at the event

$$
\mathcal { E } = \left\{ \omega \in \Omega : \operatorname* { l i m } _ { n \to \infty } \frac { S _ { n } ( \omega ) } { n } = \mu \right\} .
$$

The Strong Law of Large Numbers says that

$$
\mathrm { P } \left( { \mathcal { E } } \right) = 1 .
$$

We will prove this under the additional restriction that $\sigma ^ { 2 } = E ( X _ { j } ^ { 2 } ) <$ $\infty$ and $E ( X _ { j } ^ { 4 } ) < \infty$ .

It is no loss of generality to assume $\mu = 0$ . (Simply look at the new random variables $Y _ { j } = X _ { j } - \mu$ .) Now if

$$
\operatorname* { l i m } _ { n  \infty } \frac { S _ { n } ( \omega ) } { n } \neq 0 ,
$$

then there exist $\varepsilon > 0$ such that for infinitely many $n$

$$
\left| { \frac { S _ { n } ( \omega ) } { n } } \right| > \varepsilon .
$$

Thus to prove the theorem we prove that for every $\varepsilon > 0$

$$
\operatorname { P } \left( \left| S _ { n } \right| > n \varepsilon { \mathrm { ~ i . o . } } \right) = 0 .
$$

This then shows (by looking at the complement of this event) that

$$
\operatorname { P } ( { \mathcal { E } } ) = \operatorname { P } \left( { \frac { S _ { n } } { n } } = 0 \right) = 1 .
$$

We use the Borel-Cantelli lemma applied to the events

$$
A _ { n } = \left\{ \omega \in \Omega : | S _ { n } | \geq n \varepsilon \right\} .
$$

To estimate $\mathrm { P } ( A _ { n } )$ we use the generalized Chebyshev inequality (2) with $p = 4$ . Thus we must compute $E ( S _ { n } ^ { 4 } )$ which equals

$$
E \left( \sum _ { 1 \leq i , j , k , \ell \leq n } X _ { i } X _ { j } X _ { k } X _ { \ell } \right) .
$$

When the sums are multiplied out there will be terms of the form

$$
E ( X _ { i } ^ { 3 } X _ { j } ) , E ( X _ { i } ^ { 2 } X _ { j } X _ { k } ) , E ( X _ { i } X _ { j } X _ { k } X _ { \ell } )
$$

with $i , j , k , \ell$ all distinct. These terms are all equal to zero since $E ( X _ { i } ) = 0$ and the random variables are independent (and the subscripts are distinct). (Recall $E ( X Y ) = E ( X ) E ( Y )$ when $X$ and $Y$ are independent.) Thus the nonzero terms in the above sum are

$$
E ( X _ { i } ^ { 4 } ) { \mathrm { ~ a n d ~ } } E ( X _ { i } ^ { 2 } X _ { j } ^ { 2 } ) = \left( E ( X _ { i } ^ { 2 } ) \right) ^ { 2 }
$$

There are $n$ terms of the form $E ( X _ { i } ^ { 4 } )$ . The number of terms of the form $E ( X _ { i } ^ { 2 } X _ { j } ^ { 2 } )$ is $3 n ( n - 1 )$ .1 Thus we have shown

$$
E ( S _ { n } ^ { 4 } ) = n E ( X _ { 1 } ^ { 4 } ) + 3 n ( n - 1 ) \sigma ^ { 4 } .
$$

For $n$ sufficiently large there exists a constant $C$ such that

$$
3 \sigma ^ { 4 } n ^ { 2 } + \left( E ( X _ { 1 } ^ { 4 } ) - 3 \sigma ^ { 4 } \right) n \leq C n ^ { 2 } .
$$

(For $n$ sufficiently large, $C$ can be chosen to be $3 \sigma ^ { 4 } + 1$ .) That is,

$$
E ( S _ { n } ^ { 4 } ) \leq C n ^ { 2 } .
$$

Then the Chebyshev inequality (2) (with $p = 4$ ) together with (5) gives

$$
\mathrm { ~ P } \left( \vert S _ { n } \vert \geq n \varepsilon \right) \leq \frac { 1 } { ( n \varepsilon ) ^ { 4 } } E ( S _ { n } ^ { 4 } ) \leq \frac { C } { \varepsilon ^ { 4 } n ^ { 2 } } .
$$

Thus

$$
\sum _ { n \geq n _ { 0 } } \mathrm { P } \left( \left| S _ { n } \right| \geq n \varepsilon \right) \leq \sum _ { n \geq n _ { 0 } } { \frac { C } { \varepsilon ^ { 4 } n ^ { 2 } } } < \infty .
$$

(Here $n _ { 0 }$ is the first $n$ so that the inequality (5) holds. Since we are neglecting a finite set of terms in the sum, this cannot affect the convergence or divergence of the infinite series.) Thus by the BorelCantelli lemma

$$
\operatorname { P } \left( \left| S _ { n } \right| \geq n \varepsilon { \mathrm { ~ i . o . } } \right) = 0 .
$$

Since this holds for every $\varepsilon > 0$ we have proved the strong law of large numbers.

Remarks: Our proof assumed that the moments $E ( X _ { i } ^ { 4 } )$ and $E ( X _ { i } ^ { 2 } )$ are finite. It can be shown that the strong law of large numbers holds only under the assumption $E ( | X _ { i } | ) < \infty$ . Of course, we are still taking $X _ { i }$ to be independent with common distribution.