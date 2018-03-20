import matplotlib
matplotlib.use('TkAgg')

from matplotlib import pyplot

# prepare data
labels = ['Web', 'IOS', 'Android', 'React Native']
values = [40 ,20, 25, 15]
colors = ['red', 'green', 'gold','purple']
explode = [0,0.2, 0,0 ] #cat banh ra

#plot
pyplot.pie(values,
    labels= labels, 
    colors=colors,
    explode=explode,
    shadow=True)
pyplot.axis('equal') #thay doi truc cho tron

#show
pyplot.show()
