import wikipedia
from get_messier_object_data import ordered_messier_list
from mdutils.mdutils import MdUtils

mdFile = MdUtils(file_name='Messier_Objects', title='Messier Catalog Object Descriptions')

for object_index, messier_object in enumerate(ordered_messier_list):
    full_name = messier_object.replace("M", "Messier ")
    print(f'Creating section for # {object_index+1} of {len(ordered_messier_list)}: {full_name}...')
    mdFile.new_header(level=1, title=full_name)

    if messier_object == 'M31':
        full_name = 'Andromeda Galaxy'
    elif messier_object == 'M41':
        full_name = 'NGC 2287'

    try:
        print(f'\tAttempting to get Wikipedia summary...')
        messier_object_summary = wikipedia.summary(full_name)
    except:
        print(f'\tWikipedia summary retrieval unsuccessful...')
        messier_object_summary = '(need to add manually)'
    finally:
        print(f'\tCreating paragraph in file ...')
        print(f'\t\t{messier_object_summary}')
        mdFile.new_paragraph(messier_object_summary)
        print()

mdFile.create_md_file()