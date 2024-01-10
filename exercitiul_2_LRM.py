import pandas as pd
import matplotlib.pyplot as plt

def generate_plot_first_five():
    df = pd.read_csv('data.csv')
    df_first_five = df.head(5)

    plt.plot(df_first_five['Durata'], df_first_five['Puls'], marker='o')
    plt.xlabel('Durata')
    plt.ylabel('Puls')
    plt.title('Graficul - Primele 5 valori: Puls=f(Durata)')

    plt.show()

def generate_plot_last_nine():
    df = pd.read_csv('data.csv')
    df_last_nine = df.tail(9)

    plt.plot(df_last_nine['Durata'], df_last_nine['Puls'], marker='o')
    plt.xlabel('Durata')
    plt.ylabel('Puls')
    plt.title('Graficul - Ultimele 9 valori: Puls=f(Durata)')

    plt.show()

def generate_plot_all():
    df = pd.read_csv('data.csv')

    plt.plot(df['Durata'], df['Puls'], marker='o')
    plt.xlabel('Durata')
    plt.ylabel('Puls')
    plt.title('Graficul - Toate valorile: Puls=f(Durata)')

    plt.show()

#apelare functii
generate_plot_all()
generate_plot_first_five()
generate_plot_last_nine()
