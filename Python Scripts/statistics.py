# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 00:40:09 2015

@author: Tommy Guan
"""

    grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
    
""" Sum and Average""" 
    def grades_sum(scores):
        grades = 0
        for i in scores:
            grades += i
        return grades
        
    def grades_average(grades):
        return grades_sum(grades)/len(grades)
    
    
""" Variance """
    def grades_variance(scores):
        average = grades_average(scores)
        variance = 0
        for i in scores:
            variance += (i - average) ** 2
        return variance / len(scores)
        
    print(grades_variance(grades))

""" Standard Deviation """
    def grades_std_deviation(variance):
        return variance ** 0.5
    
    variance = grades_variance(grades)
    
    print(grades_std_deviation(variance))