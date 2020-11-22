def kmeans_cluster_housing(clusters=3):
    """Kmeans cluster a dataframe"""
    url = "https://raw.githubusercontent.com/noahgift/socialpowernba/master/data/" \
          "nba_2017_att_val_elo_win_housing.csv"
    val_housing_win_df = pd.read_csv(url)
    numerical_df = (val_housing_win_df.loc[:,["TOTAL_ATTENDENCE_MILLIONS", "ELO",
                                              "VALUE_MILLIONS", "MEDIAN_HOME_PRICE_COUNTY_MILLIONS"]])
    #scale data
    scaler =