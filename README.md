# simple-equ

An open source library containing multiple known STEM equations in a functional form. 

## Usage

simple-equ is simple, yet practical. That is the problem is solves. Sure, someone with some knowledge in their field can implement this library's
functionality. But, let us look on how that would realistically look like: 

<img width="1085" height="422" alt="quadratic" src="https://github.com/user-attachments/assets/91818279-b5af-4ad5-b9e1-1d58d5ec938f" />

<img width="1065" height="580" alt="sin" src="https://github.com/user-attachments/assets/a34229b6-628b-452f-8efa-ed1181638ffd" />

<img width="1233" height="185" alt="linearreg" src="https://github.com/user-attachments/assets/a09cc933-0e2b-493d-bbef-894115112f31" />

You just import the field of your liking, and then boom!

## Sturcture

The library is structured into fields. These fields have their own folder aka modules. However, a field can have multiple subsets. These subsets are usually 
present in the form of `python` files. For example: `algebra.py` and `geometry.py`, are examples of subfields of the general math field called **math_general**.

To import something in a practical sense in simple_equ, the structure looks like this: 

`import simple_equ.field.subfield as ...`

Practical examples include: 
`import simple_equ.math_general.geometry as sg`
`import simple_equ.economics.statistics as se` 

## Installation
```pip install simple-equ```

(For versions 3.8 or newer)

Optional: Use a venv (virtual environment). 

## Contributing

**Contributions are always welcome!**

The project encourages a community-driven approach. Everyone can contribute.
Be sure to be kind and respectful. Do not assume that something is known to the contributor
you are talking to just because you know it and do not be rude or even made comments about their
skill. This behaviour is not welcome here. 

See `contributing.md` for ways to get started.

## Features

- Community driven and open 
- Functions from different fields
- Reusable
- Highly accurate
- Simple yet practical

Do not forget to star the repo if you like it! It means a lot!
Thank you for reading this document and getting involved with our community :) 
