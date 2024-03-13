import matplotlib.pyplot as plt

def generate_bar_chart(labels, values, country):
        
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'imgs/bar_{country}.png')
    plt.show()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.savefig('imgs/pie_chart.png')
    plt.show()

if __name__ == '__main__':
    
    labels =['a', 'b', 'c']
    values = [300, 200, 100]
    
   # generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)