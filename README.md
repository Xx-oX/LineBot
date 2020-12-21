
# Secret Diary
>2020 TOC Final Project ~Line bot 

### *The Secret is, There is No Secret.*

## Introduction

A Line bot based on a finite state machine.
Keep and share your memories with others.
Or simply use it as a diary (as the name shows).

### [github repo](https://github.com/Xx-oX/Secret-Diary)

![](https://imgur.com/x5q4TXZ.png)

## Add Friend !!
![](https://imgur.com/l3FnJN1.png)
### Line id:   @373zpybw

## Finite State Machine
![fsm](https://imgur.com/FdWiSOZ.png)

## Usage

The initial state is set to `user`.
* `user`
	* Input: **"?"**
		* Reply:  an info message 
		
	* Input: **"fsm"**
		* Reply: fsm.png
		
	* Input: **"hi"**
		* Replay: a menu message

![](https://imgur.com/sdk7OZ0.png)		

* `menu`

	* 3 buttons
	
	* write, read, change

		* write: goto `write`
		
		* read: goto  `read`
		
		* change: goto `change`
		
	* Input: **"back"**
	
		* Return to `menu`

![](https://imgur.com/VC8b4dN.png)

* `write`

	* write diary for today
	
	* if is written => read only

* `read`
	
	* select date first
	
	* show the content of that day

* `change`

	* will cover the old content !!!

	* select date first

	* update the content of that day
		

## Detail

### Developing tools

use [Flask](https://flask.palletsprojects.com) as server framework

use [Line messaging API](https://developers.line.biz/en/docs/messaging-api/overview/) for main functionalities

use [Flex messgae generator](https://developers.line.biz/flex-simulator/) to design layouts

use [pipenv](https://pypi.org/project/pipenv/), [ngrok](https://ngrok.com/) as testing tools

deploy on [Heroku](https://www.heroku.com/) with app-name [`linebot-secret-diary`](https://linebot-secret-diary.herokuapp.com)


### Brief explain

[source code](https://github.com/Xx-oX/Secret-Diary)

`app.py` main program

`fsm.py` state functions and conditions, construct the fsm

`utils.py` SDK for line message API

`layout.py` define [flex message](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/) layouts (in json format) 

`database.py` a sqlite3 data base implementation, database name `diary.db`

`draw_fsm.py` draw the fsm graph of the machine

> made by [Xx-oX](https://github.com/Xx-oX)