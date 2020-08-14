#!/usr/bin/python
# -*- coding: utf8 -*-

from django.shortcuts import render, redirect
from .models import userInput, savedFile

from .forms import InputForm

from nltk.tokenize import word_tokenize

import requests


##def word_align(request):
	##return render(request,'word_alignment/word_align.html')


def inputFile(request):
	global s_token,d_token
	global num, sentences
	if request.method =='POST':
		num=0
		form = InputForm(request.POST,request.FILES)
		data=request.FILES['ifile'].read()
		text=data.decode('utf8')
		sentences=list(text.split('\r\n\r\n'))
		source, destination=sentences[0].split('\n')[0],sentences[0].split('\n')[1]
		s_token=word_tokenize(source)
		d_token=word_tokenize(destination)
		s_tokens=zip(s_token,list(range(len(s_token))))
		d_tokens=zip(d_token,list(range(len(d_token))))
		if form.is_valid():
			temp=num+1
			return render(request,'word_alignment/word_align.html',{
					's_words': s_tokens,
					'd_words': d_tokens,
					'number': temp
				})
	else:
		next_button=request.GET.get("next_button",None)
		prev_button=request.GET.get("prev_button",None)
		reverse=request.GET.get("reverse", None)
		if (next_button):
			num=num+1
			if num==len(sentences):
				num=0
			s,d=change_text(num)
			temp=num+1
			return render(request,'word_alignment/word_align.html',{
						's_words': s,
						'd_words': d,
						'number': temp
					})
		elif (prev_button):
			num=num-1
			if num==-1:
				num=len(sentences)-1
			s,d=change_text(num)
			temp=num+1
			return render(request,'word_alignment/word_align.html',{
						's_words': s,
						'd_words': d,
						'number': temp
					})
		elif (reverse):
			for i in range(len(sentences)):
				s_d=list(sentences[i].split('\r\n'))
				s_d[0],s_d[1]=s_d[1],s_d[0]
				sentence=s_d[0]+'\r\n'+s_d[1]
				sentences[i]=sentence
			s,d=change_text(num)
			temp=num+1
			return render(request,'word_alignment/word_align.html',{
						's_words': s,
						'd_words': d,
						'number': temp
					})	

		form = InputForm()
	return render(request,'word_alignment/input_file.html',{
			'form': form
		})

def downloadFile(request):
	savedfile=savedFile.objects.all().order_by('date')
	return render(request,'word_alignment/download.html',{'downloadfile':savedfile})

def change_text(number):
	source, destination=sentences[number].split('\n')[0],sentences[number].split('\n')[1]
	s_token=word_tokenize(source)
	d_token=word_tokenize(destination)
	s_tokens=zip(s_token,list(range(len(s_token))))
	d_tokens=zip(d_token,list(range(len(d_token))))
	return s_tokens, d_tokens

