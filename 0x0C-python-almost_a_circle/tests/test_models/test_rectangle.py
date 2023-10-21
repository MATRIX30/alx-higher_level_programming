#!/usr/bin/python3
"""test module for rectangle class"""

from models.rectangle import Rectangle
from models.base import Base
import unittest

from unittest.mock import patch, Mock
import io

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
        
    def test_area(self):
        """ testing the area method"""
        # assert a call to area returns an integer
        self.assertIsInstance(self.r1.area(), int)
        # assert returns right answer
        self.assertEqual(self.r1.area(), 10)
        
        
    def test_display(self):
        """test for display method"""
        r5 = Rectangle(2,2)
        
        with patch('sys.stdout',new_callable=io.StringIO) as mock_print:
            r5.display()
            
        captured_output = mock_print.getvalue()
        self.assertEqual(captured_output,"##\n##\n")
        
        r6 = Rectangle(1,1)
        
        with patch('sys.stdout',new_callable=io.StringIO) as mock_print:
            r6.display()
            
        captured_output = mock_print.getvalue()
        self.assertEqual(captured_output,"#\n")
        
        r7 = Rectangle(2,3)
        
        with patch('sys.stdout',new_callable=io.StringIO) as mock_print:
            r7.display()
            
        captured_output = mock_print.getvalue()
        self.assertEqual(captured_output,"##\n##\n##\n")
        
        r8 = Rectangle(2,3,2)
        with patch('sys.stdout',new_callable=io.StringIO) as mock_print:
            r8.display()
            
        captured_output = mock_print.getvalue()
        self.assertEqual(captured_output,"  ##\n  ##\n  ##\n")
        
        r9 = Rectangle(2,3,2,1)
        with patch('sys.stdout',new_callable=io.StringIO) as mock_print:
            r9.display()
            
        captured_output = mock_print.getvalue()
        self.assertEqual(captured_output,"\n  ##\n  ##\n  ##\n")
        
    def test___str__(self):
        """testing str method"""
        r8 = Rectangle(2,3)
        mock_obj = Mock()
        
        with patch('builtins.print', mock_obj):
            print(r8)
        
        # assert the print is called with the object 
        mock_obj.assert_called_with(r8)
        
        """verify if the right object format gets printed"""
        with patch('sys.stdout',new_callable=io.StringIO) as mock_print:
            print(r8)
            
        captured_value = mock_print.getvalue()
        self.assertEqual(captured_value,f"[Rectangle] ({r8.id}) {r8.x}/{r8.y} - {r8.width}/{r8.height}\n")
    
    def test_update_nothing(self):
        """Testing the update method"""
        r = Rectangle(2,3)
        w = r.width
        h = r.height
        r.update()
        self.assertEqual(r.width, w)
        self.assertEqual(r.height, h)
    
    def test_update(self):
        """Testing the update method"""
        r = Rectangle(2,3)
        id = r.id
        w = r.width
        h = r.height
        r.update(89)
        self.assertEqual(r.width, w)
        self.assertEqual(r.height, h)
        self.assertNotEqual(r.id, id)
        self.assertEqual(r.id, 89)
        
        #updating width
        r.update(89,2)
        self.assertEqual(r.width,2)
        
        
        #updating width
        r.update(89,2)
        self.assertEqual(r.width,2)
        
        #updating width
        r.update(89,2, 1,5)
        self.assertEqual(r.x,5)
        
        #updating width
        r.update(89,2, 1)
        self.assertEqual(r.height,1)
        
        #updating width
        r.update(89,2,1,5,4)
        self.assertEqual(r.y,4)
        
    
        
    def tearDown(self) -> None:
        return super().tearDown()