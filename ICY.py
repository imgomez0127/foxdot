Clock.bpm = 125
d2 >> play("x_o_",amp=[1,0,0.2,0])
sick_bassline = [-2,5,5.5,6,-2,-2,-2,5,5.5,6,5]
bass_rhythm = [1,0.5,0.5,1.75,0.25,0.5,0.5,0.5,0.5,1,1]
p1 >> pluck(sick_bassline,dur=bass_rhythm,oct=3)
one = [1]
hey = [0.5] + one*3 + [0.25,0.75] + one * 2 + [0.75] + one * 6 + [0.5] + one
p2 >> pluck([6],dur=hey,oct=5)
d2.stop()
p1.stop()
p2.stop()
