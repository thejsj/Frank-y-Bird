flappyBird ;
	n curPos,ln,obsPos,obsPassed,iterations,done,OPT,settings,obsTime,grav
	w #!!,?30,"Frank-y Bird"
	w !!,?25,"Press SPACE to jump..."
	w !,?25,"Press Q to quit..."
	w !,?25,"Press B for boost...",!!!
	d getDifficulty(.settings)
	s curPos("X")=5,curPos("Y")=12
	s obsPassed=0
	s obsTime=$$zFmtNum((settings("obsWidth")+settings("obsSpacing")/2),0)
	;random curPos generator here...
	f  d  q:done!OPT
	. s iterations=iterations+1
	. i (iterations#obsTime=0)!(iterations=1) d obsGen(.obsPos,.settings)    ;cada (width+spacing)/2
	. d updatePos(.curPos,.obsPos,.OPT,.obsPassed,.grav)
	. s done=$$checkPos(.curPos,.obsPos)
	. d flappyLineGen(.curPos,.obsPos,.ln)
	. d dispScreen(.ln,settings("hTime"),obsPassed)
	. i done d gameOver(obsPassed)
	q  ;
getDifficulty(settings) ;
	n difficulty,done
	f  q:done  d
	. r !,"Easy (1), Medium (2), or Hard (3)? ",difficulty
	. i difficulty=1 d
	. . s settings("hTime")=0.5,done=1
	. e  i difficulty=2 d
	. . s settings("hTime")=0.2,done=1
	. e  i difficulty=3 d
	. . s settings("hTime")=0.1,done=1
	. e  w !,"Please enter 1, 2 or 3...",!
	s settings("obsWidth")=10,settings("obsHoleHeigth")=5
	s settings("obsSpacing")=15
	q  ;
flappyLineGen(curPos,obsPos,ln) ;
	n iX,iY,curLn
	i curPos("X")=""!(curPos("Y")="") q
	f iY=2:1:23 d
	. n curLn,symbAry
	. d strGenerator(.obsPos,.symbAry,iY)
	. f iX=1:1:80 d
	. . i iX=5,(iY=curPos("Y")) s curLn=curLn_"O" q
	. . i iX=6,(iY=curPos("Y")) s curLn=curLn_">" q
	. . i $d(symbAry(iX)) s curLn=curLn_symbAry(iX) q
	. . s curLn=curLn_" "
	. s ln(iY)=curLn
	q  ;
dispScreen(ln,hTime,obsPassed) ;
	n iY,iX
	i '$d(ln(24)) d
	. f iX=1:1:80 s ln(24)=ln(24)_"^"
	w #
	f iY=2:1:23 d
	. w ln(iY)
	w ln(24)
	w "Points: ",obsPassed
	h hTime
	q  ;
updatePos(curPos,obsPos,OPT,obsPassed,grav) ;
	n in,boost ;
	s in=$$input(1,"",0,1,"","","",1,0) ;
	i in="Q" d
	. s OPT=1
	i in="B" s boost=1
	i in=" " d
	. s curPos("Y")=curPos("Y")-3,grav=0
	. s:(curPos("Y")<1) curPos("Y")=1
	e  d
	. s grav=grav+1
	. i grav>5,(grav<10) s curPos("Y")=$$zFmtNum((curPos("Y")+2),0)
	. e  i grav'<10,(grav<15) s curPos("Y")=$$zFmtNum((curPos("Y")+3),0)
	. e  i grav'<15,(grav<20) s curPos("Y")=$$zFmtNum((curPos("Y")+1),0)
	. e  s curPos("Y")=curPos("Y")+1
	d updateObsPos(.obsPos,.obsPassed,boost)
	q  ;
updateObsPos(obsPos,obsPassed,boost) ;
	n obs,obs2
	i boost d
	. f  s obs=$o(obsPos(obs)) q:obs="cnt"!(obs="")  d
	. . s obsPos(obs,"X1")=obsPos(obs,"X1")-7
	. . s obsPos(obs,"X2")=obsPos(obs,"X2")-7
	s obs=""
	f  s obs=$o(obsPos(obs)) q:obs="cnt"!(obs="")  d
	. s obsPos(obs,"X1")=obsPos(obs,"X1")-1
	. s obsPos(obs,"X2")=obsPos(obs,"X2")-1
	. i obsPos(obs,"X2")=4 s obsPassed=obsPassed+1 ;
	. i obsPos(obs,"X2")'>0 d
	. . k obsPos(obs)
	. . s obsPos("cnt")=obsPos("cnt")-1
	. . f  s obs2=$o(obsPos(obs2)) q:obs2=""!(obs2="cnt")  d
	. . . m obsPos(obs2-1)=obsPos(obs2)
	;
	q
checkPos(curPos,obsPos) ;
	n obs,dead ;
	i curPos("Y")>22 q 1
	i curPos("Y")<2 q 1
	f  s obs=$o(obsPos(obs)) q:obs="cnt"!(obs="")  d
	. i curPos("X")<obsPos(obs,"X1")!(curPos("X")>obsPos(obs,"X2")) q
	. i curPos("Y")>obsPos(obs,"Y1"),(curPos("Y")<obsPos(obs,"Y2")) q
	. s dead=1
	q dead
obsGen(obsPos,settings) ;
	n cnt
	s cnt=obsPos("cnt")+1,obsPos("cnt")=cnt
	s obsPos(cnt,"Y1")=$r(18)+1
	s obsPos(cnt,"Y2")=obsPos(cnt,"Y1")+settings("obsHoleHeigth")
	i cnt>1 d
	. s obsPos(cnt,"X1")=obsPos(cnt-1,"X2")+settings("obsSpacing")
	e  s obsPos(cnt,"X1")=80
	s obsPos(cnt,"X2")=obsPos(cnt,"X1")+settings("obsWidth")
	q  ;
strGenerator(obsPos,symbAry,iY) ;
	n obs,Xi
	f  s obs=$o(obsPos(obs)) q:obs="cnt"!(obs="")  d
	. i obsPos(obs,"X1")']""!(obsPos(obs,"X2")']"") q
	. i iY>obsPos(obs,"Y1"),(iY<obsPos(obs,"Y2")) q
	. i iY=obsPos(obs,"Y1")!(iY=obsPos(obs,"Y2")) d  q
	. . f Xi=obsPos(obs,"X1"):1:obsPos(obs,"X2") s symbAry(Xi)="="
	. s symbAry(obsPos(obs,"X1"))="|",symbAry(obsPos(obs,"X2"))="|"
	. f Xi=(obsPos(obs,"X1")+1):1:(obsPos(obs,"X2")-1) s symbAry(Xi)="."
	q  ;
gameOver(obsPassed) ;
	n name,i,top5,repeat,out ;
	w !!,?30,"GAME OVER"
	w !,?31,"Total: ",obsPassed,!!
	w ?24,"Enter your initials: "
	r "","",name#3
	w !!,?28,"HALL OF FAME" ;
	s name=$$up(name)
	i '$d(^XFSJ(name))!(^XFSJ(name)<obsPassed) s ^XFSJ2(obsPassed,name)="",^XFSJ(name)=obsPassed
	f  s top5=$o(^XFSJ2(top5),-1) q:top5=""  d  q:out=5     ;top five
	. f  s repeat=$o(^XFSJ2(top5,repeat)) q:repeat=""  d  q:out=5
	. . s out=out+1
	. . w !,?25,out_".  ",repeat_"   [ "_^XFSJ(repeat)_" ]"
	q
	q  ;;#eor#