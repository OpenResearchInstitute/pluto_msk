Bit rate:
$$ T_b = 1/F_b $$



𝝿t/2Tb
𝝿tFb/2
2𝝿tFb/4
ωbt/4

\\[
\begin{align*}
s(t) = a_I cos(\pi t/2T_b) cos(2\pi f_0t) + a_Q sin(\pi t/2T_b) sin(2\pi f_0t) \\
	 = a_I 1/2 (cos(2\pi f_0t - \pi t/2T_b) + cos(2\pi f_0t + \pi t/2T_b)) + \\
	   a_Q 1/2 (cos(2\pi f_0t - \pi t/2T_b) - cos(2\pi f_0t + \pi t/2T_b))
\end{align*}
\\]

where $$ a_X \in { -1, 1 } $$ a_I=a_Q or $$aI = -aQ -> aN = 1$$ when aI=aQ or aN = -1 when aI = -aQ


\\[
\begin{align*}
s(t) = cos(2\pi f_ct + \alpha_n \pi t/2T_b + \phi_n)
\end{align*}
\\]

where

$$
\alpha_n =
\begin{cases}
-1 	&\text{if \(a_I = a_Q\)} \\
1 &\text{else}
\end{cases}
$$

$$
f_n =
\begin{cases}
a &\text{if \(n = 0\)\} \\
r\cdot f_{n-1} &\text{else} \\
\end{cases}
$$

aI = aQ = 1

s(t) = 0.5*(cos(2𝝿f0t - 𝝿t/2Tb) + cos(2𝝿f0t + 𝝿t/2Tb) + cos(2𝝿f0t - 𝝿t/2Tb) - cos(2𝝿f0t + 𝝿t/2Tb))
     = cos(2𝝿f0t - 𝝿t/2Tb) 

aI = 1;  aQ = -1

s(t) = 0.5*(cos(2𝝿f0t - 𝝿t/2Tb) + cos(2𝝿f0t + 𝝿t/2Tb)) - 
       0.5*(cos(2𝝿f0t - 𝝿t/2Tb) - cos(2𝝿f0t + 𝝿t/2Tb))
     = 0.5*(cos(2𝝿f0t - 𝝿t/2Tb) + cos(2𝝿f0t + 𝝿t/2Tb) - cos(2𝝿f0t - 𝝿t/2Tb) + cos(2𝝿f0t + 𝝿t/2Tb))
     = cos(2𝝿f0t + 𝝿t/2Tb)

aI = -1; aQ = 1

s(t) = -0.5*(cos(2𝝿f0t - 𝝿t/2Tb) + cos(2𝝿f0t + 𝝿t/2Tb)) +
        0.5*(cos(2𝝿f0t - 𝝿t/2Tb) - cos(2𝝿f0t + 𝝿t/2Tb))
     =  0.5*(-cos(2𝝿f0t - 𝝿t/2Tb) - cos(2𝝿f0t + 𝝿t/2Tb) + cos(2𝝿f0t - 𝝿t/2Tb) - cos(2𝝿f0t + 𝝿t/2Tb))
     = -cos(2𝝿f0t + 𝝿t/2Tb)
     =  cos(2𝝿f0t + 𝝿t/2Tb + 𝝿)


aI = aQ = -1

s(t) = -0.5*(cos(2𝝿f0t - 𝝿t/2Tb) + cos(2𝝿f0t + 𝝿t/2Tb)) +
	   -0.5*(cos(2𝝿f0t - 𝝿t/2Tb) - cos(2𝝿f0t + 𝝿t/2Tb))
	 =  0.5*(-cos(2𝝿f0t - 𝝿t/2Tb) - cos(2𝝿f0t + 𝝿t/2Tb) - cos(2𝝿f0t - 𝝿t/2Tb) + cos(2𝝿f0t + 𝝿t/2Tb))
	 = -cos(2𝝿f0t - 𝝿t/2Tb) 
	 =  cos(2𝝿f0t - 𝝿t/2Tb + 𝝿)


s(t) = cos(2𝝿f0t + a[n]𝝿t/2Tb + φ[n])
     = cos(2𝝿(f0 + a[n]fb/4)t + φ[n])

where a[n] ∈ {1, -1} and φ[n] ∈ {0, 𝝿}

As a result there are four possible values for s(t):

 cos(2𝝿(f0 + fb/4)t)
-cos(2𝝿(f0 + fb/4)t)
 cos(2𝝿(f0 - fb/4)t)
-cos(2𝝿(f0 - fb/4)t)

where f1 = f0 - fb/4 and f2 = f0 + f_b/4 resulting in


 cos(2𝝿f1t)
-cos(2𝝿f1t)
 cos(2𝝿f2t)
-cos(2𝝿f2t)


When demodulating the receive samples are mixed with both f1 and f2 at 0 degree phase (cosine)


 cos(2𝝿f1t)*cos(2𝝿f1t)
-cos(2𝝿f1t)*cos(2𝝿f1t)
 cos(2𝝿f2t)*cos(2𝝿f1t)
-cos(2𝝿f2t)*cos(2𝝿f1t)

 cos(2𝝿f1t)*cos(2𝝿f2t)
-cos(2𝝿f1t)*cos(2𝝿f2t)
 cos(2𝝿f2t)*cos(2𝝿f2t)
-cos(2𝝿f2t)*cos(2𝝿f2t)



The four resulting values for the f1 mix are


cos(2𝝿f1t)*cos(2𝝿f1t) = 1/2 [ cos(2𝝿f1t - 2𝝿f1t) + cos(2𝝿f1t + 2𝝿f1t) ]
					  = 1/2 [ cos(0) + cos(4𝝿f1t) ]
					  = 1/2 [ 1 + cos(4𝝿f1t)]

-cos(2𝝿f1t)*cos(2𝝿f1t) = -1/2 [ cos(2𝝿f1t - 2𝝿f1t) + cos(2𝝿f1t + 2𝝿f1t) ]
					   = -1/2 [ cos(0) + cos(4𝝿f1t) ]
					   = -1/2 [ 1 + cos(4𝝿f1t)]

(both the previous results are a DC value and a sinusoid at 2*f1)

cos(2𝝿f2t)*cos(2𝝿f1t) = 1/2 [ cos(2𝝿f2t - 2𝝿f1t) + cos(2𝝿f2t + 2𝝿f1t) ]
					  = 1/2 [ cos(2𝝿(f2 - f1)t)t + cos(2𝝿(f2 + f1)t) ]

-cos(2𝝿f2t)*cos(2𝝿f1t) = -1/2 [ cos(2𝝿f2t - 2𝝿f1t) + cos(2𝝿f2t + 2𝝿f1t) ]
					   = -1/2 [ cos(2𝝿(f2 - f1)t)t + cos(2𝝿(f2 + f1)t) ]

(both are sinusoids at (f2-f1) and (f2+f1))

we are only interested in the DC value


as part of the Costas loops the receive samples are also mixed with f1 and f2 at 90 degree phase (sin)


 cos(2𝝿f1t)*sin(2𝝿f1t + theta)
-cos(2𝝿f1t)*sin(2𝝿f1t + theta)
 cos(2𝝿f2t)*sin(2𝝿f1t + theta)
-cos(2𝝿f2t)*sin(2𝝿f1t + theta)


The four resulting values are

cos(2𝝿f1t)*sin(2𝝿f1t) = 1/2 [ sin(2𝝿f1t + 2𝝿f1t + theta) - sin(2𝝿f1t - 2𝝿f1t + theta) ]
					  = 1/2 [ sin(4𝝿f1t + theta) - sin(theta) ]
					  = 1/2 sin(4𝝿f1t + theta)


-cos(2𝝿f1t)*sin(2𝝿f1t) = -1/2 [ sin(2𝝿f1t + 2𝝿f1t) - sin(2𝝿f1t - 2𝝿f1t) ]
					   = -1/2 [ sin(4𝝿f1t) - sin(0) ]
					   = -1/2 sin(4𝝿f1t)

again we only care about the DC component, which when the phases are aligned is 0. If the phases are not aligned the 
sin(0) term becomes sin(Δφ) a constant.


cos(2𝝿f1t)*sin(2𝝿f1t) = 1/2 [ sin(2𝝿f2t + 2𝝿f1t) - sin(2𝝿f2t - 2𝝿f1t) ]
					  = 1/2 [ sin(2𝝿(f2+f1)t) - sin(2𝝿(f2-f1)t) ]


cos(2𝝿f1t)*sin(2𝝿f1t) = -1/2 [ sin(2𝝿f2t + 2𝝿f1t) - sin(2𝝿f2t - 2𝝿f1t) ]
					  = -1/2 [ sin(2𝝿(f2+f1)t) - sin(2𝝿(f2-f1)t) ]



