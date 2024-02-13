  1 def isStackFull() :
  2     global SIZE, stack, top
  3     if (top >= SIZE-1) :
  4         return True
  5     else :
  6         return False
  7
  8 def isStackEmpty() :
  9     global SIZE, stack, top
 10     if (top == -1) :
 11         return True
 12     else :
 13         return False
 14
 15 def push(data) :
 16     global SIZE, stack, top
 17     if (isStackFull()) :
 18         print("¿¿¿ ¿ ¿¿¿¿")
 19         return
 20     top += 1
 21     stack[top] = data
 22
 23 def pop() :
 24     global SIZE, stack, top
 25     if (isStackEmpty()) :
 26         print("¿¿¿ ¿¿¿¿¿")
 27         return None
 28     data = stack[top]
 29     stack[top] = None
 30     top -= 1
 31     return data
 32
 33 def peek() :
 34     global SIZE, stack, top
 35     if (isStackEmpty()) :
 36         print("¿¿¿ ¿¿¿¿¿.")
 37         return None
 38     return stack[top]
 39
 40 SIZE = int(input("¿¿ ¿¿¿ ¿¿¿¿¿==>"))
 41 stack = [None for _ in range(SIZE)]
 42 top = -1
~
