a
    5T�`�  �                	   @   s�  d dl Z e �d� e �d� e �d� e �d� e �d� e �e jdkrLdnd	� d dlZd dlZd dlZd dlZd dlZ	e�
d
�Ze�
d�Zeej� ed�Zeejv r�ne�  e �e jdkr�dnd	� dd� Zed� e�� ZdZdZdZdZd Zd Zeed � ed� ed� ed� zd dlZW n   eed � Y n0 eed � eed � ed�Zedk�r eed �Zee�ZdZee�ZdZdZ dZ!ee!�Z!d Z"ee"�Z"d!Z#ee#�Z#e$e�D �]ZZ%d"Z%e$e�D ]Z&e%e�'e�7 Z%�q�e$e!�D ]
Z&d"Z(�q�e$e!�D ]Z&e(e�'e�7 Z(�qe$e!�D ]
Z&d"Z)�q$e$e!�D ]Z&e)e�'e �7 Z)�q8e$e"�D ]
Z&d"Z*�qVe$e"�D ]Z&e*e�'e�7 Z*�qje$e#�D ]
Z&d"Z+�q�e$e#�D ]Z&e�'e�Z+�q�e+e% d# d$ e( d# d% e) d# e* Z,eee, � e-d&d'��Z.e.�/e,d( � W d  � n1 �s0    Y  �q�ed)k�r�ed*�Z0ed+�Zee�ZdZee�ZdZdZ dZ!ee!�Z!d Z"ee"�Z"d!Z#ee#�Z#e$e�D �]$Z%d"Z%e$e�D ]Z&e%e�'e�7 Z%�q�e$e!�D ]
Z&d"Z(�q�e$e!�D ]Z&e(e�'e�7 Z(�q�e$e!�D ]
Z&d"Z)�q�e$e!�D ]Z&e)e�'e �7 Z)�q�e$e"�D ]
Z&d"Z*�qe$e"�D ]Z&e*e�'e�7 Z*�q*e$e#�D ]
Z&d"Z+�qHe$e#�D ]Z&e�'e�Z+�q\e0e% d# d$ e( d# d% e) d# e* Z,ee,� ed� �q�dS ),�    Nzpkg install requestszpkg install secretszpkg install syszpkg install jsonzpkg install time�nt�cls�clearz!https://pastebin.com/raw/R6Cvh21Yz!https://pastebin.com/raw/XhuMr4EXz
[+]Pasword Bnwsa : c                 C   s2   | d D ]$}t j�|� t j��  t�d� qd S )N�
gUUUUUU�?)�n�stdout�write�flush�mm�sleep)�M�c� r   �3C:\Users\AHMED\Desktop\New-folder(5)\Create-Card.py�slow   s    
r   z�
===========================================
|   [Developer] => : AhmadDev             |
|   [Insta] => : Jev0m                    |
|   [Telegram Developer] => : @Div0mbot   |
===========================================
z[1;31mz[1;32mz[0;94mz[1;33mzTTb: bo zanen ka cardaka esh daka yan na aw linkay xwarawa copy ka la google paste ka� zhttp://www.ke1.nl/en/checker/z[-] pip install randomz1 - Drust krdne Card Randomz'2 - Drwst Krdne Card Ba Daxil Krdne Binz[+] Kama Bzhardat Awe 1 Or 2 : �1z[+] Chand Cardt Awe : Z15Z
1234567890Z123456�3�6� �|�0Z202zvisacheck.txt�ar   �2z2[+] Enter the first six digits of the card type : z[+] Enter Count : )1�os�system�nameZrequestsZsecretsZjson�sysr   �timer
   �get�g�s�print�text�inputZaskv�exitr   ZsessionZrs�R�G�B�YZnuZrandomZalno3Zamount�intZlength�charsZchars2Zlength2Zlength3Zlength4�rangeZpassword�itemZchoiceZmonthZyaerZpasswordbinZashai�b�open�xr   Zawalsttar8amr   r   r   r   �<module>   s�   









(2
(