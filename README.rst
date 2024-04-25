==============
Pyxels Library
==============

Summary
-------------------------------
Pyxels is a Python library for manipulating colors in the RGB color space.


Description
--------------------

Pyxels provides a simple and intuitive API for creating, manipulating, and comparing 
colors in the RGB color space. With Pyxels, you can perform arithmetic operations on 
colors, convert colors between different color spaces, and more. Whether you're 
building a digital art project, a game, or a web app, Pyxels makes it easy to work 
with colors in Python.

Pyxels is currently in early development, and may not yet be ready for general use.


Installation
------------

To install Pyxels, you can use pip:

.. code:: bash

   pip install pyxels


Usage
-----

pyxels.RGB
~~~~~~~~~~

The ``pyxels.RGB`` class represents a color in the RGB color space. It
has three attributes: ``red``, ``green``, and ``blue``, which are all
integers between 0 and 255. It supports addition, subtraction,
multiplication, and division with other ``pyxels.RGB`` instances, as
well as comparison with other ``pyxels.RGB`` instances.


.. code:: python

   from pyxels import RGB

   # Create a new RGB color
   color = RGB(255, 0, 0)

   # Add two RGB colors
   new_color = color + RGB(0, 255, 0)

   # Blend two RGB colors
   blended_color = color.blend(new_color, 0.42)

   # Check if two RGB colors are equal
   print(f"The colors are {'equal' if color == new_color else 'not equal'}")

   # Convert an RGB color to a hex string
   print(color.to_hex())

   # Load an RGB color from a hex string
   color = RGB.from_hex("#C0FFEE")

   # Set the least significant bit of each color channel
   other_color = RGB(254, 127, 63)
   other_color.set_lsb(RGB(1, 0, 1))

   # Get the least significant bit of each color channel
   lsb = other_color.get_lsb()

   # Bitwise XOR two RGB colors
   xor_color = color ^ new_color


License
-------



Pyxels is released under the MIT license. 
See `LICENSE <LICENSE>`__ for more information.

