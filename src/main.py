import data_processing as dp
import user_interaction as ui 
import db_operations as db_ops

if __name__ =="__main__":
    data = dp.read_csv('data/nypd-arrest-data-2018-1.csv')
    while True:
        choice = ui.get_user_input()
        match choice:
            case '1':
                offences = dp.count_offences(data)
                print("Top 10 Offences: ")
                print(sorted(offences.items(), key=lambda x: x[1], reverse=True)[:10] + "\n")
            case '2':
                age_pd_cd = dp.arrest_count_age_pd_cd(data)
                print("Fourth greatest number of arrests by PD_CD for each age group: ")
                fourth_highest = {}
                for age, pd_dict in age_pd_cd.items():
                    sorted_arrests = sorted(pd_dict.items(), key=lambda x: x[1], reverse=True)
                    if len(sorted_arrests) >= 4:
                        fourth_highest[age] = sorted_arrests[3]
                print(fourth_highest)  # Prints all the fourth highest arrests by age group
            case '3':
                offence_desc = ui.get_offence_desc()
                filtered_data = dp.filter_by_offence(data, offence_desc)
                if filtered_data:
                    dp.export_to_csv(filtered_data, f"{offence_desc}.csv" + "\n")
                else:
                    print("No data available for this description" + "\n")
            case '4':
                db_ops.create_db_and_table()
                db_ops.insert_in_db(data)
            case '5':
                break
            case _:
                print('Unrecognised option' + "\n")