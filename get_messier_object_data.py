import pandas as pd
import math


ordered_messier_list = ["M45", "M74", "M77", "M31", "M32", "M110", "M33", "M76", "M52", "M103", "M34", "M79", "M42",
                        "M43", "M78", "M1", "M41", "M93", "M47", "M46", "M50", "M48", "M35", "M37", "M36", "M38", "M95",
                        "M96", "M105", "M65", "M66", "M101", "M63", "M51", "M94", "M102", "M3", "M64", "M53", "M59",
                        "M60", "M87", "M89", "M90", "M58", "M84", "M86", "M88", "M91", "M98", "M99", "M100", "M85",
                        "M49", "M61", "M104", "M68", "M44", "M83", "M67", "M5", "M13", "M92", "M57", "M56", "M29",
                        "M39", "M27", "M71", "M107", "M12", "M10", "M14", "M9", "M4", "M80", "M19", "M62", "M11", "M26",
                        "M16", "M17", "M18", "M24", "M81", "M82", "M23", "M21", "M20", "M8", "M25", "M28", "M22", "M69",
                        "M70", "M54", "M55", "M75", "M6", "M7", "M15", "M2", "M72", "M73", "M97", "M108", "M40", "M106",
                        "M109", "M30"]

if __name__ == '__main__':
    messier_wikipedia_page = 'https://en.wikipedia.org/wiki/Messier_object'
    webpage_data_frame = pd.read_html(messier_wikipedia_page)
    print(f'Length of ordered_messier_list = {len(ordered_messier_list)}')

    messier_data_frame = webpage_data_frame[1]
    print(messier_data_frame.info())
    select_data = messier_data_frame.loc[:, ['Object type', 'Constellation', 'Distance (kly)', 'Common name']]

    messier_numbers = messier_data_frame['Messier number'].str.split('[', expand=True)[0]
    select_data['Messier number'] = messier_numbers

    prefix = "var PasteText = ["
    with open('messier_list.txt', 'w') as file:
        for messier_object in ordered_messier_list:
            row_number = select_data[select_data['Messier number'] == messier_object].index[0]
            print(f'Row number of {messier_object} = {row_number}')
            if messier_object == ordered_messier_list[0]:
                row_string = prefix
            else:
                row_string = len(prefix)*' '
            row_string = row_string + "tr(\"" + select_data['Object type'][row_number].capitalize()
            row_string = row_string + ' in ' + select_data['Constellation'][row_number]
            if len(select_data['Common name'][row_number]) > 1:
                row_string = row_string + " — " + select_data['Common name'][row_number]
            if not math.isnan(select_data['Distance (kly)'][row_number]):
                kly_distance = select_data['Distance (kly)'][row_number]
                print(kly_distance)
                if kly_distance >= 1000:
                    distance = kly_distance / 1000
                    unit = 'Mly'
                elif kly_distance < 1:
                    distance = kly_distance * 1000
                    unit = 'ly'
                else:
                    distance = kly_distance
                    unit = 'kly'
                row_string = row_string + f" [{distance:.0f} {unit}]"
            row_string = row_string + "\"),"
            row_string = row_string + "\t// " + messier_object
            if messier_object != ordered_messier_list[-1]:
                row_string = row_string + '\n'
            else:
                row_string = row_string + '];\n'
            file.write(row_string)


