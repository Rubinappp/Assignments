#Student entity
full_name="Rubina Poudel"
age=21
cgpa=3.9
current_semester="8"
enrollment_status="Open"
print(f"Name:{full_name} {type(full_name)}")
print(f"Age:{age} {type(age)}")
print(f"CGPA: {cgpa } {type(cgpa)}")
print(f"Current Semester:{current_semester} {type(current_semester)}")
print(f"Enrollment Status:{enrollment_status} {type(enrollment_status)}")

age="22"
print(f"Age:{age} {type(age)}")






# 1. How does Python’s dynamic typing influence memory allocation and runtime behavior?

# - Variables do not store values directly,they store references to objects in memory. Each object carries:value,type and reference count. Object is allocated on heap at run time.
# - Since everything in python is object it Uses more memory than statically-typed and runtime type checking makes it slower.


# 2. Why is strict type enforcement preferred in system-level software but not in scripting
# languages?
# System-Level Software (C,C++): Strict Typing:
# - Performance: No runtime type checking so faster execution, compiler optimizes ahead of time
# - Safety: Type errors caught before running 
# - Predictability: Exact memory usage known beforehand which is critical for embedded systems/OS

# Scripting Languages (Python, JavaScript) : Dynamic Typing:

# Fast development: Don't declare types, write code quickly.Speed of writing code > speed of running code
# Flexibility: Same code handles different types, processes varied inputs
# Lower risk: Script crashes don't bring down systems, easy to fix .



