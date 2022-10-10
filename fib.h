#ifndef N
#	error "N not defined"
#	define R (-1)
#elif N < 0 || N > 19
#	error "N not in range 0-19"
#	define R (-1)
#else

#	if N == 1
#		define R 0
#	elif N == 2
#		define R 1
#	else

#		ifndef I	
#			define I 2
#			define T1 0	
#			define T2 1
#		endif

#		if I == N
#			define TO_R
#			include "helper_add_ts.h"

#			undef I
#			undef T1
#			undef T2
#			undef TT
#		else
#			define TO_TT
#			include "helper_add_ts.h"

#			define T2_TO_T1
#			include "helper_copy.h"
#			define TT_TO_T2
#			include "helper_copy.h"

#			include "helper_incr_i.h"
#			include "fib.h"

#		endif
#	endif
#endif