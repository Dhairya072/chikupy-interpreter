# Linked List vs Arrays

Both are generic data structures, which can be used to store any type of data.
Linked list can store data of Type T, and Array can store data of Type T.

### Array
* | 1 | 2 | 3 | 4 | 5 |
* O(1) indexing
* Worst case O(n) insertion/deletion
* Amortized O(1) insertion/deletion
* Wastage of memory, if allocated 100 cells and use only 5 cells
* Array are processor friendly due to spatial locality(For small arrays, linear search is faster than binary search)

### Linked List
* 1 -> 2 -> 3 -> 4 -> 5 -> null
* O(n) indexing
* O(1) insertion/deletion

## Refrential Transparency
```python
A = [1,2,3,4,5]
B = A
B.append(10)
print(A) # [1,2,3,4,5,10]
```
In the above example, A and B are pointing to the same memory location. So, if we change B, A will also change.

Cheap Assignment => A changes if B changes, No referencial transparency

Refrencial Transparency => B is a separate array. Expensive Assignment

One way -> Store a slice of A in B and when something is pushed to A nothing changes in B.

In swift, we have Copy on Write(COW) semantics. If we assign A to B, A and B will point to the same memory location. If we change B, A will not change. If we change A, B will not change.
Makes copy when changes happen. Delay the copy until you write.

In C++, we have vectors. Vectors have O(1) append time if enough memory is allocated to vectors. If not, it will allocate more memory and copy the elements from old vector to new vector. This is expensive.

## For Linked List
```
A <- Linked List
B = A
A.push(1)
print(B)
```

`push` pushes on the head of A.
Do tail sharing in linked list.
In assignment, make to pointer to head.
When element is pushed, make a new node and point the head to the new node.
A -> 1->2->3->4->5->null
B -> 1->2->3->4->5->null

B.push(0)
A -> 1->2->3->4->5->null
B -> 0->(A)1->2->3->4->5->null

> Insertion at head is only efficient insertion.

```
XS: List[T]
a: T
cons(a, XS): List[T]
```

> is-empty, head, tail are constant time operations

<br/>

# First-Class Functions
Functions should be allowed to use as other data types.

```python
def foo(x):
	return 2*x*x + 3*x + 5

def derivative(f):
	dx = 0.0001
	def df(x): return (f(x+dx) - f(x))/dx
	return df

dfoo = derivative(foo)
print(dfoo(2))
```

```python
def make_counter(init=0):
	def inc():
		nonlocal init
		init += 1
	def dec():
		nonlocal init
		init -= 1
	def get():
		nonlocal init
		return init
	return inc, dec, get

inc1, dec1, get1 = make_counter()
inc2, dec2, get2 = make_counter(5)

inc1()
inc1()
inc2()
dec1()
inc2()
print(get1(), get2()) # 1 7
```

This program will not work on a stack.
- Init only exists in the scope of make_counter
- But scope of make counter is destroyed after it returns.
- So, init is destroyed. But we are using it after the scope is destroyed.
- Init escapes it lexical scope. As it is accessible outside the scope with inc, dec, get.

What python does it recognizes that init is used outside the scope and it creates init separately and when stack of make_counter is destroyed it will not destroy init.

In previous program, f also escapes the scope of derivative. dfoo uses f which is not defined in the scope of dfoo.