import matplotlib.pyplot as plt
import seaborn as sns

class DataManager:
    """ Data presentation class.
    """
    def __init__(self, data, main='Name'):
        self.__data = data
        self.__main = main

    def show_sample(self, entries=10):
        return self.__data.sample(entries)

    def show_titles(self, entries=10):
        return self.__data[self.__main].sample(entries)

    def feature_list(self):
        return self.__data.dtypes

    def show_counter(self, criteria):
        return self.__data[criteria].value_counts()

    def describe_some_data(self, features):
        return self.__data[features].describe()

    # Specific for video game sales dataset
    def show_same_title(self, title):
        # Example showing repeated titles
        vg_data = self.__data
        name = self.__main
        selection = vg_data[[name]] == title
        return vg_data[selection.all(1)]

    # Specific for video game sales dataset
    def same_titles_counter(self):
        vg_data = self.__data
        name = self.__main
        # First we find out which video games have beeen released on multiple platforms
        multiplatform_titles = vg_data[vg_data[name].duplicated(keep=False)]
        return multiplatform_titles[name].value_counts()

    def plot_counts(self, variable, title):
        # Counting releases of video games by platform
        plt.figure(figsize=(12,6))
        plt.title(title)
        sns.countplot(y=variable, data=self.__data, order=self.__data[variable].value_counts().index)

    def plot_counts_top_n(self, variable, title, n_counts=20):
        # Counting releases of video games by platform
        plt.figure(figsize=(12,6))
        plt.title(title)
        sns.countplot(y=variable, data=self.__data, order=self.__data[variable].value_counts().iloc[:n_counts].index)

    def plot_histogram(self, variable, title):
        selection = self.__data[variable].notna()
        notna_data = self.__data[selection]
        plt.figure(figsize=(22,8))
        plt.title(title)
        sns.countplot(data=notna_data[variable], x=notna_data[variable].astype(int), order = range(notna_data[variable].min().astype(int),notna_data[variable].max().astype(int)))

    def plot_data_per_variable(self, x_name, title, n_counts=20):
        # set values
        vg_data = self.__data
        y_name = self.__main
        # Top selling games globally. Note the dataset is already sorted by number of global sales
        plt.figure(figsize=(12,6))
        plt.title(title)
        sns.barplot(x=x_name,y=y_name,data=vg_data.sort_values([x_name],ascending=False).loc[:n_counts])

    def plot_data_per_variable_filtering(self, x_name, pivot, filters, title, n_counts=20):
        # set values
        set_filter = self.__data[pivot]==filters
        vg_data = self.__data[set_filter]
        y_name = self.__main
        # Top selling games globally. Note the dataset is already sorted by number of global sales
        plt.figure(figsize=(12,6))
        plt.title(title)
        sns.barplot(x=x_name, y=y_name, data=vg_data.iloc[:n_counts])

    def plot_sales_same_game(self, filters, n_counts=20):
        # set values
        set_filter = self.__data['Name']==filters
        vg_data = self.__data[set_filter]
        # Top selling games globally. Note the dataset is already sorted by number of global sales
        plt.figure(figsize=(12,6))
        plt.title('Total Global Sales of '+filters+' over different platforms')
        sns.barplot(x='Global_Sales', y='Platform', data=vg_data.iloc[:n_counts])

    def plot_data_per_variable_grouping(self, x_name, y_name, title, n_counts=20):
        # set values
        set_filter = self.__data.groupby(y_name, as_index=False).sum().sort_values(x_name, ascending=False)[:n_counts]
        # Top selling games globally. Note the dataset is already sorted by number of global sales
        plt.figure(figsize=(12,6))
        plt.title(title)
        sns.barplot(x=x_name, y=y_name, data=set_filter)

    def plot_data_box(self, x_name, y_name, title, n_counts=20):
        # set values
        vg_data = self.__data
        # Top selling games globally. Note the dataset is already sorted by number of global sales
        plt.figure(figsize=(12,6))
        plt.title(title)
        sns.boxplot(data=vg_data,y=y_name, x=x_name)

    def plot_stacked_bar(self, x_var, y_var, criteria, title, n_counts=20):
        #set seaborn plotting aesthetics
        plt.figure(figsize=(12,6))
        plt.title(title)
        sns.set(style='white')
        #create stacked bar chart
        #self.__data.set_index(variable).plot(kind='bar', stacked=True)
        ax = sns.histplot(self.__data, x=x_var, hue=y_var, weights=criteria, multiple='stack', palette='tab20c', shrink=0.8)
        sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))

    def plot_pie(self, x_var, y_var, title, n_counts=20):
        data = self.__data[[x_var, y_var]].groupby(x_var, as_index=False).sum().reset_index()[:n_counts]
        data.sort_values(by=y_var, ascending=False)
        plt.figure(figsize=(24,12))
        plt.pie(x=data[y_var], autopct='%1.2f%%')#, labels=)
        plt.legend(data[x_var], loc="right", bbox_to_anchor=(1.2, 1.05))
        plt.title(title)
        plt.show()

    def plot_histogram_with_range(self, variable, title, max_range=10):
        # Plotting the global sales of video games with less than 10 million global sales in USD
        plt.figure(figsize=(18,6))
        plt.title(title)
        sns.histplot(data=self.__data[variable], binwidth=0.05, binrange=[0,max_range])
