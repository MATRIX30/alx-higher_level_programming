#!/usr/bin/python3
"""test module for rectangle class"""

from models.rectangle import Rectangle
from models.base import Base
import unittest


class TestRectangle(unittest.TestCase):
    """Test class for Rectangle class"""
    
    def setUp(self) -> None:
        """creating 2 rectangle instance objects to be used
        throughout our test for rectangle class
        """
        self.r1 = Rectangle(2,5)
        self.r2 = Rectangle(8,14,1,3)
        self.r3 = Rectangle(8,14,1,3,25)
    
    
    def test_inheritance_from_base(self):
        "testing if rectangle inherites from base class"
        self.assertEqual(issubclass(Rectangle,Base), True)

    def test_constructor(self):
        """test various aspects of the constructor"""
        # verify if initializing with negative width raises value error
        self.assertRaises(ValueError, Rectangle,-1,4,4,5)
        
        # verify if initializing with negative length raises value error
        self.assertRaises(ValueError, Rectangle,1,-4,4,5)
        
        #test constructor with default values for id
        self.assertEqual(self.r1.id + 1,self.r2.id)
        self.assertEqual(self.r3.id,25)
        
        # testing getter and setter for width
        self.assertEqual(self.r1.width,2)
        self.r1.width = 4
        self.assertEqual(self.r1.width,4)
        
        # testing getter and setter for height
        self.assertEqual(self.r1.height,5)
        self.r1.height = 12
        self.assertEqual(self.r1.height,12)
        
        # testing defualt values for x and y is zero
        self.assertEqual(self.r1.x,0)
        self.r1.width = 4
        self.assertEqual(self.r1.y,0)
        
        # testing getter and setter for x and y
        self.assertEqual(self.r2.x,1)
        self.r2.x = 4
        self.assertEqual(self.r2.x,4)
        
        # testing getter and setter for x and y
        self.assertEqual(self.r2.y,3)
        self.r2.y = 4
        self.assertEqual(self.r2.y,4)
        
    def test_validate_attributes(self):
        """ validating all the attributes"""
        # validating for the right type 
        self.assertRaises(TypeError, Rectangle,10, "2")
        self.assertRaises(TypeError, Rectangle,"3", 4)
        self.assertRaises(TypeError, Rectangle,"10", "2")
        
        self.assertRaises(TypeError, Rectangle,2.5, 2)
        self.assertRaises(TypeError, Rectangle,"3", 4.5)
        self.assertRaises(TypeError, Rectangle,2, 5.4)
        
        self.assertRaises(TypeError, Rectangle,float('inf'), 5.4)
        
        # validating for the right value
        self.assertRaises(ValueError, Rectangle,0,4,3,5)
        self.assertRaises(ValueError, Rectangle,1,0,4,5)
        self.assertRaises(ValueError, Rectangle,-8,4,3,5)
        self.assertRaises(ValueError, Rectangle,1,-7,4,5)
        self.assertRaises(ValueError, Rectangle,1,4,-4,5)
        self.assertRaises(ValueError, Rectangle,1,4,4,-5)
        
        
        
        
        
    def tearDown(self) -> None:
        return super().tearDown()