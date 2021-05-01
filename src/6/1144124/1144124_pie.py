from matplotlib import pyplot as plt

def pie():

    hasil = 1144124 % 3 + 2
    
    potong = [7,8,2,12]
    kegiatan = ['Kuliner','Kuliah','Bioskop','Nongkrong']
    kolom = ['c','m','y','g']
    
    for i in range(1, hasil+1):
        plt.subplot(2,2,i)
        plt.pie(potong,
        labels=kegiatan,
        colors=kolom,
        startangle=90,
        shadow= True,
        explode=(0,0,0.2,0),
        autopct='%1.1f%%')         
        plt.title('Kegiatan Sehari-hari')
        plt.subplots_adjust(hspace=.4)
    
    plt.show()
    