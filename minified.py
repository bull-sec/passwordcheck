# -*- coding: utf-8 -*-
import sys
b=len
A=None
f=True
import re
B=re.search
import getpass
C=getpass.getpass
def P(T):
 n=b(T)<8
 i=B(r"\d",T)is A
 R=B(r"[A-Z]",T)is A
 H=B(r"[a-z]",T)is A
 o=B(r"[ !#!#$%&'()@£¬*+,-./[\\\]^_`{|}~"+r'"]',T)is A
 z=not(n or i or H or R or o)
 return{'password_ok':z,'length_ok':n,'upper_error':R,'lower_error':H,'digits_error':i,'symbols_error':o,}
def I():
 T=C("Enter the password to test: ")
 q=P(T)
 for k,v in q.items():
  print(k,'-->',v)
 if q['password_ok']!=f:
  print("\nNOT ACCEPTABLE")
 else:
  print("\nIS ACCEPTABLE")
 del T
if __name__=='__main__':
 I()