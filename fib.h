#define STR_HELPER(x) #x
#define STR(x) STR_HELPER(x)
#define INC STR(__INCLUDE_LEVEL__)

#ifndef N
#	error "N not defined"
#else

// #pragma message INC "-N: " STR(N)

#	if N == 0
#		define R 0
#	elif N == 1
#		define R 1
#	else

//		r1 = fib(n - 1)
#		pragma region
//			n = n - 1
#			include "helper_sub_n.h"

//			store n
#			pragma message " STORING N @" INC " -> " STR(N)
#			include "helper_store_n.h"

//			r = fib(n)
#			pragma message INC "-NA: " STR(N)
// #			include "fib.h"

//			r1 = r
#			define DEST 1
#			include "helper_store_r.h"
#		pragma endregion

//		n = load n
#		define LOAD
#		include "helper_store_n.h"
#		pragma message " LOADING N @" INC " -> " STR(N)

//		r2 = fib(n - 2)
#		pragma region
//			n = n - 1
#			include "helper_sub_n.h"

//			r = fib(n)
// #			pragma message INC "-NB: " STR(N)
// #			include "fib.h"

//			r2 = r
#			define DEST 2
#			include "helper_store_r.h"
#		pragma endregion

//		r = r1 + r2
#		include "helper_add_rs.h"
#	endif

// #pragma message INC "-R: " STR(R)

#endif