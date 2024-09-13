import pandas as pd
import matplotlib.pyplot as plt


#EDA Functions

#Find average rating for each movie
def findAvgRating():
    avg_ratings = df.groupby(['MovieID', 'Title'])['Rating'].mean().reset_index()
    avg_ratings = avg_ratings.sort_values('Rating', ascending=False)
    return avg_ratings.to_string(index=False, justify='left', col_space=[10, 50, 10])

#Identify top 5 movies with the highest average rating
def top5Movies():
    top_5_movies = df.groupby(['MovieID', 'Title'])['Rating'].mean().reset_index()
    top_5_movies = top_5_movies.sort_values('Rating', ascending=False)
    top_5_movies = top_5_movies.head(5)
    return(top_5_movies.to_string(index=False, justify='left', col_space=[10, 50, 10]))

#Determine distribution of ratings across all movies
def rating_dist():
    # Calculate the distribution of ratings
    rating_distribution = df['Rating'].value_counts().sort_index()

    # Calculate the percentage of each rating
    rating_percentage = (rating_distribution / len(df)) * 100

    # Create a DataFrame to display the results
    rating_dist_df = pd.DataFrame({
        'Count': rating_distribution,
        'Percentage': rating_percentage
    })

    return(rating_dist_df)

#Find most popular genre of movies
def pop_genre():
    pop_genre = df['Genre'].value_counts().head(1)
    return(pop_genre)

def rating_trend_by_year():
    # Extract year from Timestamp
    df['Year'] = df['Timestamp'].dt.year

    # Group by year and calculate average rating
    yearly_ratings = df.groupby('Year')['Rating'].mean().reset_index()

    # Sort by year
    yearly_ratings = yearly_ratings.sort_values('Year')

    # Calculate the overall trend
    trend = yearly_ratings['Rating'].diff().mean()

    # Identify years with highest and lowest average ratings
    highest_year = yearly_ratings.loc[yearly_ratings['Rating'].idxmax()]
    lowest_year = yearly_ratings.loc[yearly_ratings['Rating'].idxmin()]

    # Prepare the result string
    result = "Average ratings by year:\n"
    result += str(yearly_ratings) + "\n\n"
    result += f"Overall trend: {'Increasing' if trend > 0 else 'Decreasing'} by {abs(trend):.4f} per year\n\n"
    result += f"Year with highest average rating: {highest_year['Year']} ({highest_year['Rating']:.2f})\n"
    result += f"Year with lowest average rating: {lowest_year['Year']} ({lowest_year['Rating']:.2f})"

    return result


#ADVANCED ANALYSIS Functions

#Top 5 users who have rated most movies
def top5Users():
    top_5_users = df.groupby('UserID')['MovieID'].count().sort_values(ascending=False).head(5)
    print(top_5_users)

#Determine most common rating given by users
def mostCommonRating():
    most_common_rating = df['Rating'].mode()[0]
    print(most_common_rating)

#Determine any correlations between user ratings and genre
def genreCorrelation():
    # Group by genre and calculate average rating
    genre_ratings = df.groupby('Genre')['Rating'].mean().reset_index()
    print(genre_ratings)



#VISUALIZATION

#Create bar chart showing top 5 movies with highest average rating
def top5MoviesChart():
    top_5_movies = findAvgRating().head(5)
    plt.figure(figsize=(12, 6))
    bars = plt.bar(top_5_movies['Title'], top_5_movies['Rating'])
    plt.xlabel('Movie Title')
    plt.ylabel('Average Rating')
    plt.title('Top 5 Movies with Highest Average Rating')
    plt.xticks(rotation=45, ha='right')
    
    # Set y-axis limits dynamically
    y_min = top_5_movies['Rating'].min() * 0.9  # 10% below the lowest rating
    y_max = top_5_movies['Rating'].max() * 1.1  # 10% above the highest rating
    plt.ylim(y_min, y_max)
    
    plt.tight_layout()
    
    # Add value labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                 f'{height:.2f}',
                 ha='center', va='bottom', fontsize=8)
    
    plt.show()

#Plot distribution of ratings using histogram
def rating_dist_hist():
    print("filler")
    

#Visualize the trend of movie ratings using line chart
def rating_trend_line():
    # Group by year and calculate average rating
    df['Year'] = df['Timestamp'].dt.year
    yearly_ratings = df.groupby('Year')['Rating'].mean().reset_index()
    
    plt.figure(figsize=(12, 6))
    plt.plot(yearly_ratings['Year'], yearly_ratings['Rating'], marker='o')
    plt.xlabel('Year')
    plt.ylabel('Average Rating')
    plt.title('Trend of Movie Ratings Over Time')
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Set y-axis limits dynamically
    y_min = yearly_ratings['Rating'].min() * 0.9  # 10% below the lowest rating
    y_max = yearly_ratings['Rating'].max() * 1.1  # 10% above the highest rating
    plt.ylim(y_min, y_max)
    
    # Add value labels for each point
    for x, y in zip(yearly_ratings['Year'], yearly_ratings['Rating']):
        plt.text(x, y, f'{y:.2f}', ha='center', va='bottom', fontsize=8)
    
    plt.tight_layout()
    plt.show()


#Create pie chart showing distribution of movies across genres
def genre_pie():
    # Count the number of movies in each genre
    genre_counts = df['Genre'].value_counts()

    # Create a pie chart
    plt.figure(figsize=(10, 8))
    plt.pie(genre_counts.values, labels=genre_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title('Distribution of Movies Across Genres')
    
    # Equal aspect ratio ensures that pie is drawn as a circle
    plt.axis('equal')  
    
    # Adjust layout to fit better on screen
    plt.tight_layout(pad=1.5)
    
    # Adjust text size for better readability
    plt.rcParams['font.size'] = 8
    
    # Use a legend instead of labels for better space utilization
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    
    plt.show()



#OPTIONAL

#implement a simple recommendation of movies based on past ratings
def recommendation_app():
    # Get unique genres
    genres = df['Genre'].unique()

    # Display available genres
    print("Available genres:")
    for i, genre in enumerate(genres, 1):
        print(f"{i}. {genre}")

    # Prompt user for genre choice
    while True:
        try:
            choice = int(input("Enter the number corresponding to your chosen genre: "))
            if 1 <= choice <= len(genres):
                chosen_genre = genres[choice - 1]
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Filter movies by chosen genre and find the highest rated
    genre_movies = df[df['Genre'] == chosen_genre]
    highest_rated = genre_movies.loc[genre_movies['Rating'].idxmax()]

    highest_rated = highest_rated.copy()
    highest_rated['Year'] = pd.to_datetime(highest_rated['Timestamp']).year


    # Display result
    print(f"\nThe highest rated movie in the {chosen_genre} genre is:")
    print(f"Title: {highest_rated['Title']}")
    print(f"Rating: {highest_rated['Rating']:.2f}")
    print(f"Year: {highest_rated['Year']}")

    input("\nPress Enter to continue...")
    

#DATA CLEANING
def data_cleaning(df):    
    # Check for missing values
    #print(df.isnull().sum())

    # Handle missing values by filling with appropriate values
    df['Rating'] = df['Rating'].fillna(df['Rating'].mean())
    df['Title'] = df['Title'].fillna('Unknown Title')

    # Verify that there are no missing values left
    #print(df.isnull().sum())

    #convert the timestamp to a usable date format
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='s')

    return df

# def EDA():
#     while True:
#         # Display the menu
#         print("EDA Menu:")
#         print("1. Find average rating for each movie")
#         print("2. Identify top 5 movies with the highest average rating")
#         print("3. Determine distribution of ratings across all movies")
#         print("4. Find most popular genre of movies")
#         print("5. Analyze how ratings have changed over time (grouping by year)")
#         print("6. Back to Main Menu")

#         # Get the user's choice
#         choice = input("Enter your choice (1-6): ")
#         match choice:
#             case "1":
#                 print("Finding average ratings...")
#                 avg_ratings = findAvgRating()
#                 print(avg_ratings)
#                 input("Press any key to continue...")
#             case "2":
#                 print("Identifying top 5 movies with highest average rating...")
#                 top5Movies()
#                 input("Press any key to continue...")
#             case "3":
#                 print("Determining distribution of ratings across all movies...")
#                 rating_dist()
#                 input("Press any key to continue...")
#             case "4":
#                 print("Finding most popular genre of movies...")
#                 pop_genre()
#                 input("Press any key to continue...")
#             case "5":
#                 print("Analyzing how ratings have changed over time...")
#                 rating_trend_by_year()
#                 input("Press any key to continue...")
#             case "6":
#                 print("Returning to main menu...")
#                 break
#             case _:
#                 print("Invalid choice. Please enter a number between 1 and 5.")

# def AdvAnalysis():
#     while True:
#         # Display the menu
#         print("Advanced Analysis Menu:")
#         print("1. Top 5 users who have rated most movies")
#         print("2. Determine most common rating given by users")
#         print("3. Determine any correlations between user ratings and genre")
#         print("4. Back to Main Menu")

#         # Get the user's choice
#         choice = input("Enter your choice (1-4): ")
#         match choice:
#             case "1":
#                 print("Identifying top 5 users who have rated most movies...")
#                 top5Users()
#                 input("Press any key to continue...")
#             case "2":
#                 print("Determining most common rating given by users...")
#                 mostCommonRating()
#                 input("Press any key to continue...")
#             case "3":
#                 print("Determining correlations between user ratings and genre...")
#                 genreCorrelation()
#                 input("Press any key to continue...")
#             case "4":
#                 print("Returning to main menu...")
#                 break
#             case _:
#                 print("Invalid choice. Please enter a number between 1 and 4.")

# def Visualization():
#     while True:
#         # Display the menu
#         print("Visualization Menu:")
#         print("1. Creating bar chart showing top 5 movies with highest average rating...")
#         print("2. Plotting distribution of ratings using histogram...")
#         print("3. Visualizing the trend of movie ratings using line chart...")
#         print("4. Creating pie chart showing distribution of movies across genres...")
#         print("5. Back to Main Menu")

#         # Get the user's choice
#         choice = input("Enter your choice (1-5): ")

#         match choice:
#             case "1":
#                 print("Creating bar chart showing top 5 movies with highest average rating...")
#                 top5MoviesChart()
#                 input("Press any key to continue...")
#             case "2":
#                 print("Plotting distribution of ratings using histogram...")
#                 rating_dist_hist()
#                 input("Press any key to continue...")
#             case "3":
#                 print("Visualizing the trend of movie ratings using line chart...")
#                 rating_trend_line()
#                 input("Press any key to continue...")
#             case "4":
#                 print("Creating pie chart showing distribution of movies across genres...")
#                 genre_pie()
#                 input("Press any key to continue...")
#             case "5":
#                 print("Returning to main menu...")
#                 break
#             case _:
#                 print("Invalid choice. Please enter a number between 1 and 5.")




#import the dataset
df = pd.read_csv("MovieAnalysis\movie_ratings_dataset.csv", sep=',')


df = data_cleaning(df)


# while True:
#     # Display the menu
#     print("Main Menu:")
#     print("1. Exploratory Data Analysis")
#     print("2. Advanced Analysis")
#     print("3. Visualization")
#     print("4. Recommendation System")
#     print("5. Exit")

#     # Get the user's choice
#     choice = input("Enter your choice (1-5): ")

#     match choice:
#         case "1":
#             print("Performing Exploratory Data Analysis...")
#             EDA()
#         case "2":
#             print("Performing Advanced Analysis...")
#             # Call the function for Advanced Analysis
#             AdvAnalysis()
#         case "3":
#             print("Generating Visualizations...")
#             # Call the function for Visualization
#             Visualization()
#         case "4":
#             print("Running Recommendation System...")
#             # Call the function for Recommendation System
#             recommendation_app()
#         case "5":
#             # Exit the program
#             print("Exiting the program...")
#             exit()
#         case _:
#             print("Invalid choice. Please enter a number between 1 and 5.")
