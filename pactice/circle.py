import matplotlib.pyplot as plt
 
figure, axes = plt.subplots()
circle1 = plt.Circle( (0, 0 ),10 ,fill = False )
circle2 = plt.Circle( (0, 40 ),50 ,fill = False )
circle3 = plt.Circle( (0, 90 ),100 ,fill = False )
plt.xlim([-200,200])
plt.ylim([-50,200])
axes.set_aspect( 1 )
axes.add_artist( circle1 )
axes.add_artist( circle2 )
axes.add_artist( circle3 )
plt.title( 'Circles' )
plt.show()