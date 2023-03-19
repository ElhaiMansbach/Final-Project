from tree import Tree
from data_handler import data_handler
from sql_database import *
from abstract_Database import Abstract_Database

class Calculator:
    '''This static class performing all the calculations'''
    
    
    
    @staticmethod
    def get_voter_count(db:Abstract_Database) -> int: 
        '''
        How much people votes
        
        >>> # When nobody votes
        >>> Calculator.get_voter_count()
        0
        >>> # When 200 users votes
        >>> Calculator.get_voter_count()
        200
        '''
        return 0
    
    
    @staticmethod
    def get_voter_count_by_gender(db:Abstract_Database) -> list[int]:  # [male,female]
        '''
        Get the number of voters by gender
        
        >>> # When nobody votes
        >>> Calculator.get_voter_count_by_gender()
        >>> # [MALE, FEMALE]
        [0, 0]
        >>>> # When 2 males users votes 
        >>> Calculator.get_voter_count_by_gender()
        [2,0]
        '''
        return [0, 0]

    
    @staticmethod
    def get_voter_count_by_age(db:Abstract_Database) -> list[int]:
        '''
        Get the number of voters by age group
        
        >>> # When nobody votes
        >>> Calculator.get_voter_count_by_age()
        >>> # 18-25, 26-35, 36-45, 46-55, 56-65, 66+
        [0, 0, 0, 0, 0, 0]
        >>> # When 2 users votes between 18-25 age 
        >>> Calculator.get_voter_count_by_age()
        [2, 0, 0, 0, 0, 0]
        '''
        return [0, 0, 0, 0, 0, 0]
        
    