#!/usr/bin/env python3

from person import Person

import io
import sys

class TestPerson:
    '''Person in person.py'''

    def test_is_class(self):
        '''is a class with the name "Person".'''
        guido = Person(name='Guido', job='Sales')  # Provide both name and job
        assert(type(guido) == Person)
        
    def test_name_not_empty(self):
        '''prints "Name must be string between 1 and 25 characters." if empty string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(name="", job="Sales")  # Provide both name and job
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Name must be a string between 1 and 25 characters.\n")

    def test_name_string(self):
        '''prints "Name must be string between 1 and 25 characters." if not string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(name=123, job='Sales')  # Provide both name and job
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Name must be a string between 1 and 25 characters.\n")

    def test_name_under_25(self):
        '''prints "Name must be string between 1 and 25 characters." if string over 25 characters.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(name="What do Persons do on their day off? Can't lie around - that's their job.", job='Sales')  # Provide both name and job
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Name must be a string between 1 and 25 characters.\n")

    def test_valid_name(self):
        '''saves name if string between 1 and 25 characters.'''
        guido = Person(name="Guido", job="Sales")  # Provide both name and job
        assert(guido.name == "Guido")

    def test_valid_name_title_case(self):
        '''converts name to title case and saves if between 1 and 25 characters'''
        guido = Person(name="guido van rossum", job="Sales")  # Provide both name and job
        assert(guido.name == "Guido Van Rossum")

    def test_job_not_in_list(self):
        '''prints "Job must be in list of approved jobs." if not in job list.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        Person(name="Guido", job="Benevolent dictator for life")  # Provide both name and job
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Job must be in list of approved jobs.\n")

    def test_job_in_list(self):
        '''saves job if in job list.'''
        guido = Person(name="Guido", job="ITC")  # Provide both name and job
        assert(guido.job == "ITC")