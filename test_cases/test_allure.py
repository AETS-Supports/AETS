#!/usr/bin/env python3
# -*- coding:utf-8  -*-
"""

"""

import logging as log
import pytest
import allure

@allure.step("测试步骤1:step")
def step1():
    print("步骤1")
    
@pytest.fixture(scope='session',autouse=True)
def db():
    print('预制条件')

    
@allure.epic("项目名称: AETS")
@allure.feature("模块：AllureModule1")
@allure.story("功能描述：demo1")
class Testdome1(object):
    @allure.title("用例标题：title")
    def test_dome_1(self):
        '''用例一的用例描述: 我是第一个用例，我只有一个步骤'''
        db()
        print("第一个测试用例")
        step1()
        
    @allure.title("用例标题：title")
    def test_dome_2(self):
        '''用例一的用例描述: 我是第一个用例，我只有一个步骤'''
        print("第一个测试用例")
        step1()
       
@allure.epic("项目名称: AETS")
@allure.feature("模块：AllureModule2")
class Testdome2(object):
    def test_dome_2(self):
        '''用例一的用例描述: 我是第一个用例，我只有一个步骤'''
        print("第一个测试用例") 
        step1()
        
# @allure.story("story")
# @allure.title("title")
# @allure.description("description")
# @allure.description_html("html")
# @allure.id("id")
# @allure.issue("issue")
# @allure.label("label")
# @allure.link("link")
# @allure.manual("manual")
# @allure.parent_suite("parent_suit")
# @allure.suite("suit")
# @allure.sub_suite("sub_suit")
# @allure.severity("serverity")
# @allure.tag("tag")
