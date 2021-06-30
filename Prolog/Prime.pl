is_prime(2). is_prime(3). is_prime(P) :- integer(P),
P > 3,
P mod 2 =\= 0,
\+ has_factor(P,3).

% has_factor(N,L) :- N has an odd factor F >= L.
%	(integer, integer) (+,+)

has_factor(N,L) :- N mod L =:= 0.
