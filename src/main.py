import data_processing as dp
import user_interaction as ui 
import db_operations as db_ops

# Main execution start
if __name__ == '__main__':

    # Read data from .csv to dictionary list
    data = dp.read_csv('../data/nypd-arrest-data-2018-1.csv')
    
    # Endless option loop unless break oprtion to quit
    while True:
        
        # Get user choice and trigger corresponding requirement
        choice = ui.get_user_input()
        match choice:
            
            # Count offences and show top 10
            case '1':
                offences = dp.count_offences(data)
                print("\nTop 10 Offences: ")
                print(sorted(offences.items(), key=lambda x: x[1], reverse=True)[:10])
            
            # Show 4th greatest number of arrests by PD_CD for each age group
            case '2':
                age_pd_cd = dp.arrest_count_age_pd_cd(data)
                print("\n Fourth greatest number of arrests by PD_CD for each age group: ")
                fourth_highest = {}
                for age, pd_dict in age_pd_cd.items():
                    sorted_arrests = sorted(pd_dict.items(), key=lambda x: x[1], reverse=True)
                    if len(sorted_arrests) >= 4:
                        fourth_highest[age] = sorted_arrests[3]
                print(f"{fourth_highest} \n") 
            
            # Filter data by offence description and export to .csv
            case '3':
                offence_desc = ui.get_offence_desc()
                filtered_data = dp.filter_by_offence(data, offence_desc)
                if filtered_data:
                    dp.export_to_csv(filtered_data, f"{offence_desc}.csv \n")
                    print(f"Data successfully exported to {offence_desc}.csv \n")
                else:
                    print("No data available for this description \n")
            
            # Create database and insert data
            case '4':
                db_name = "nypd_arrests.db"
                db_ops.create_db_and_table(db_name)
                db_ops.insert_in_db(data, db_name)
            
            # Exit program
            case '5':
                break
            
            # Unrecognised action contingency
            case _:
                print('Unrecognised option' + "\n")