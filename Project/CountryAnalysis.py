import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("covid.csv",index_col = 1)
ind=list(set(data.index))

def Analysis (country,choice):
    if country in ind:
        if choice == 'new_cases' or choice == 'total_cases' or choice == 'new_deaths' or choice == 'total_deaths':
            Graf_gen(country,choice)
        else:
            print("Plese enter a valid choice")
    else:
        print("Please enter a valid country name in camel case!!!")


def Graf_gen(country,choice):
    cnt_data = data.loc[country]
    date = cnt_data['date']
    date = [i for i in range(len(list(date)))]
    new_cases = cnt_data[choice]
    if choice == "new_cases":
        plt.ylabel("Number of new cases per day")
        title = "Daily new cases trend in " + country
    elif choice == 'total_cases':
        plt.ylabel("Total cases")
        title = "Total cases trend in " + country
    elif choice == 'new_deaths':
        plt.ylabel("Deaths happening daily")
        title = "Daily death trend in " + country
    elif choice == 'total_deaths':
        plt.ylabel("Total deaths")
        title = "Total deaths trend in " + country
    plt.title(title)
    plt.plot(date,new_cases)
    plt.xlabel("Number of Days")
    
    plt.savefig(country+".png",dpi=1000)
    plt.show()
            
country = input("Enter the country(use camel case): ")
print("Enter new_cases for daily cases\nEnter total_cases total cases\nEnter new_deaths daily death happning\nEnter total_deaths for total deaths happened over time")
choice = input("Enter your choice: ")

Analysis(country,choice)
            