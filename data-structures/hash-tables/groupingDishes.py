# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 01:16:34 2020

@author: Logan Rowe
"""
def groupingDishes(dishes):
    dish_dict={}
    for dish in dishes:
        dish_dict[dish[0]]=dish[1:]
    
    ingredients=[]
    for value in dish_dict.values():
        ingredients.extend(value)
    
    #Lets narrow our list down to only ingredients that are in 2 or more dishes
    ingredient_dict={ingredient:[] for (ingredient,count) in zip(set(ingredients),[ingredients.count(ingredient) for ingredient in set(ingredients)]) if count>1}
    
    for key in [*dish_dict.keys()]:
        for value in dish_dict[key]:
            for ingredient in ingredient_dict:
                if ingredient == value:
                    ingredient_dict[ingredient]=[*ingredient_dict[ingredient],key]    
                    
    ingredient_dict=[[key]+[*sorted(ingredient_dict[key])] for key in ingredient_dict]
    ingredient_dict=sorted(ingredient_dict)
    
    return(ingredient_dict)
    




if __name__=='__main__':
    dishes=[["Pasta","Tomato Sauce","Onions","Garlic"], 
         ["Chicken Curry","Chicken","Curry Sauce"], 
         ["Fried Rice","Rice","Onions","Nuts"], 
         ["Salad","Spinach","Nuts"], 
         ["Sandwich","Cheese","Bread"], 
         ["Quesadilla","Chicken","Cheese"]]
    
    print(groupingDishes(dishes))