# SmartBedRoom
this is a class project, a simple integration of LED, motor, light sensor...,etc. 
acturely, it's a alarmclock with speaker, button, motor, webui.

The speaker is use to play music as normal alarm clock.

Button is use to stop the alarmclock, 
I suppose that user can't find their smart phone and use it turn off the alarm,
and also, the button help user easily turn on alarmclock again
(the time will be at the same time on the nextday)
os I decide to setup a physical button.

The motor is the function which I like best.
I use it to open the curtain, I wish to bring the light into my bedroom,
and the the light 'pre' wake me up slowly.

The Web ui is implement by django,
but acturely there is some problem I cannot fix it gracefully.
something like, reload-problem, that stop me to get contorl instances form __builtit__ .
And I use "--nothreading", with out this django paramater, 
the django was no response when I use execute it in a thread.

