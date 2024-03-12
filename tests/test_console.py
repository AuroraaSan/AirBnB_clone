#!/usr/bin/python3
"""
Unit tests for console that check console for capturing stdout into a StringIO object
"""

import os
import sys
import unittest
from unittest.mock import create_autospec, patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestConsole(unittest.TestCase):
    """
    Unittest for the console model
    """

    def setUp(self):
        """Redirecting stdin and stdout"""
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)
        self.err = ["** class name missing **",
                    "** class doesn't exist **",
                    "** instance id missing **",
                    "** no instance found **",
                    ]

        self.cls = ["BaseModel",
                    "User",
                    "State",
                    "City",
                    "Place",
                    "Amenity",
                    "Review"]

    def create(self, server=None):
        """
        Redirects stdin and stdout to the mock module
        """
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def last_write(self, nr=None):
        """Returns last n output lines"""
        if nr is None:
            return self.mock_stdout.write.call_args[0][0]
        return "".join(map(lambda c: c[0][0],
                           self.mock_stdout.write.call_args_list[-nr:]))

    def test_quit(self):
        """Quit command"""
        cli = self.create()
        self.assertFalse(cli.onecmd("quit"))

    def test_help(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("help")
            output = f.getvalue().strip()
            self.assertTrue("Documented commands (type help <topic>):" in output)

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 36)  # UUID length

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            output = f.getvalue().strip()
            obj_id = output

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd(f"show BaseModel {obj_id}")
            output = f.getvalue().strip()
            self.assertTrue("BaseModel" in output)

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            output = f.getvalue().strip()
            obj_id = output

        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd(f"destroy BaseModel {obj_id}")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

if __name__ == '__main__':
    unittest.main()
