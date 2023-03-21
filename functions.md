# Functions

### Without free variable
```Ocaml
fun add(a, b) = a + b in add(2,3) end
```
This expr evaluates to 5

In python
```python
def add(a,b):
	return a + b

add(2,3)
```

Scope is where the binding is introduced and can be used.

```python
def foo(a):
	return a+1

print(foo(2))

def fact(n):
	if n <= 1: return1
	return n*fact(n-1)

print(fact(5))

def even(n):
	match n:
		case 0: return True
		case 1: return False
		case _: return odd(n-1)

# print(even(5)) # error: odd is not defined

def odd(n):
	match n:
		case 0: return False
		case 1: return True
		case _: return even(n-1)

print(even(5))
```

In python if we dont evaluated the function it can be called but need to be defined before calling it.

```python
def even(n):
	match n:
		case 0: return True
		case 1: return False
		case _: return xoo(n-1)

def odd(n):
	match n:
		case 0: return False
		case 1: return True
		case _: return even(n-1)

print(even(1))
```
This outputs False.

For mutually recursive functions, we should define the function before calling it. Forward Declaration is used.

Forward Declaration:
```cpp
#include <bits/stdc++.h>

using namespace std;

bool even(int n){
	if(n==0) return true;
	if(n==1) return false;
	return xoo(n-1); // Gives error: 'xoo' was not declared in this scope
}

int main()
{
	cout<<even(1);
	return 0;
}
```
Correct Implementation:
```cpp
#include <bits/stdc++.h>

using namespace std;
bool odd(int n);
bool even(int n){
	if(n==0) return true;
	if(n==1) return false;
	return odd(n-1);
}
bool even(int n){
	if(n==0) return false;
	if(n==1) return true;
	return even(n-1);
}

int main()
{
	cout<<even(1);
	return 0;
}
```

OCaml:
```OCaml
let f x = x+1
let f y = f y + 2;
```

Not recursive
f 3 outputs 6

For recursive explicitly add "rec" keyword.

```OCaml
open Printf

let rec even = function
	| 0 -> true
	| 1 -> false
	| n -> odd (n-1)
and odd = function
	| 0 -> false
	| 1 -> true
	| n -> even (n-1)
in printf "%B" (even 25)

let () in = printf "%B\n" (even 25)
```

```OCaml
let rec f args1 = body1
and g args2 = body2
in expr
```
Both f and g are valid in body1, body2 and expr.

Python is byte code interpreted language. It is written in c. Python generates byte code which is then executed by C.

```python
if age == old:
	use explicit # Am I old?
else:
	use implicit
```

```OCaml
let identity x = x;;
(* identity : 'a -> 'a = <fun> *)
```
---

```Python
@dataclass
class LetFun:
	name: 'AST'
	params: List['AST']
	body: 'AST'
	expr: 'AST'

@dataclass
class FunCall:
	fn: 'AST'
	args: List['AST']

@dataclass
class FnObject:
	params: List['AST']
	body: 'AST'


class eval:
	...
	case LetFun(Variable(name), params, body, expr):
		environment.enter_scope()
		environment.add(name, FnObject(params,body))
		v = eval_(expr)
		environment.exit_scope()
		return v
	case FunCall(Variable(name), args):
		fn = environment.get(name)
		argv = []
		for arg in args:
			argv.append(eval_(arg))
		environment.enter_scope()
		for param, arg in zip(fn.params, argv):
			environment.add(param.name, arg)
		v = eval_(fn.body)
		environment.exit_scope()
		return v
		


e = LetFun(
	f, [a,b],
	BinOp(a, '+', b),
	FunCall(f, [NumLiteral(2), NumLiteral(3)])
	)

```

```
letfun f(a,b) =
	if a then 0 else b
in
	f(true, 3/0)
end
```

if output is 0 then call by name,
if output is error then call by value.

```
letfun f(a, lazy b) =
	if a then 0 else b
```
lazy makes it call by-name

# Hate all languages 

Weird Scoping in python
```Python
x = 1
y = x
x = 2
print(y) #1

def foo(n):
	return 0

bar = foo

def foo(n):
	return 1

print(bar(1)) # 0

def fact(n):
	return 1 if n <= 1 else n*fact(n-1)

baz = fact

def fact(n):
	return 1

print(baz(3)) # 3
```

Local Reasoning
It is possible to reason about a small piece of code without knowing the entire program.
- Python is not local reasoning friendly.
- Haskell is local reasoning friendly.


```Python
def fact(n):
	return 1 if n <= 1 else n*fact(n-1)

deg = fact

def baz():
	def fact(n):
		return 1
	print(deg(3))

baz() # 6
```
Here fact works recursively when baz is called.

```OCaml
open Printf

let fact n = 0
let g = fact
let fact n = 1
let () = printf "%d\n" (g 3)
let rec fact n = if n <= 1 then 1 else n*fact(n-1)
let g = fact
let fact n = 1
let () = printf "%d\n" (g 3)

(* Output: 0 6 *)
```

### Think how python works in prev example

```
fact: 16
baz = fact: 16
fact: 21
baz(3)-> fact:16(3)

env:{
	"fact": fact:21
	"baz": fact:16
}
```

When we first call baz it calls rec fact. Then the rec fact calls the fact:21.

This can be done with resolution binding. But it will break the odd/even example.
Resolution and late binding can't be done simultaneously.

For mutual recursion,
- Forward declaration is used.
- Late binding is used.
- Explicitly declaring mutually recursive functions. Like in OCaml using "and" keyword.

File -> Lexer -> Parser -> Resolver -> TypeChecker? -> Evaluator

```Python
class Variable:
	def __init__(self, name):
		self.name = name
		self.id = fresh()
def resolve(program, environment):
	if environment is None:
		environment = Environment()

	def resolve_(program):
		return resolve(program, environment)
	match program:
		case Variable(name):
			return environment.get(name)
		case Let(Variable(name) as v, value, expr):
			re1 = resolve_(value)
			environment.enter_scope()
			environment.add(name, v)
			re2  = resolve_(expr)
			environment.exit_scope()
			return Let(v, re1, re2)

```