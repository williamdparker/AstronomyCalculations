# Pull out the planet circle draw into a separate function in order to bump out individual planets and maybe
# draw an arrow from the planet to the ruler below


import json
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


def read_json_file(data_file):
    # Open and read the JSON file
    with open(data_file, "r") as file:
        json_data = json.load(file)
    return json_data


def draw_logarithmic_ruler(object_distances, object_diameters):
    # Calculate the extreme distance values
    min_distance = min(object_distances.values())
    max_distance = max(object_distances.values())

    # Define the range for the logarithmic scale
    log_min = np.floor(np.log10(min_distance))
    log_max = np.ceil(np.log10(max_distance))

    # Generate the logarithmic ruler
    fig, ax = plt.subplots(figsize=(10, 5))
    # ax.set_xscale('log')
    ax.set_xlim(log_min, log_max)
    ax.set_ylim(-0.45, 0.15)

    x_limits = ax.get_xlim()
    y_limits = ax.get_ylim()

    x_range = np.diff(x_limits)[0]
    y_range = np.diff(y_limits)[0]

    # # Major and minor ticks positioned on top and directed inward
    # ax.xaxis.set_ticks_position('top')
    # ax.xaxis.set_label_position('top')
    # ax.xaxis.set_major_locator(plt.LogLocator(base=10.0))
    # ax.xaxis.set_minor_locator(plt.LogLocator(base=10.0, subs=np.arange(2, 10) * 0.1))
    # ax.tick_params(axis='x', which='major', size=15, width=2, direction='in', pad=-15, labelsize=12)
    # ax.tick_params(axis='x', which='minor', size=7, width=1, direction='in', pad=-15)
    #
    # # Set custom tick labels for major ticks (1, 10, 100, ...)
    # labels = [0.01, 0.1, 1, 10, 100]
    # ax.set_xticklabels(labels)
    #
    # # Move tick labels lower
    # ax.tick_params(axis='x', which='major', labelrotation=0, labelcolor='black', length=10, width=2, direction='in',
    #                 pad=-30)


    # Hide x-axis
    ax.get_xaxis().set_visible(False)
    # Hide y-axis
    ax.get_yaxis().set_visible(False)

    # Draw rectangle representing the ruler background
    ax.add_patch(plt.Rectangle((x_limits[0], y_limits[0]), x_range, 0.5*y_range, edgecolor='black',
                               facecolor='none', linewidth=5))

    # Add axis at top of rectangle
    ax_top = ax.inset_axes([x_limits[0], y_limits[0] + 0.49*y_range, x_range, 0.001],
                           transform=ax.transData, zorder=2)

    # Hide the y-axis and unnecessary spines
    ax_top.get_yaxis().set_visible(False)
    ax_top.spines['top'].set_visible(False)
    ax_top.spines['right'].set_visible(False)
    ax_top.spines['left'].set_visible(False)

    # ax_top.set_xscale("log")
    ax_top.set_xlim(x_limits)
    # ax_top = ax.secondary_xaxis('top')
    ax_top.xaxis.set_major_locator(ticker.LogLocator(base=10.0, numticks=10))
    ax_top.set_xticks([np.log10(0.2), np.log10(0.5), 0, np.log10(2), np.log10(5), 1, np.log10(20), np.log10(50)])
    ax_top.set_xticklabels(['0.2', '0.5', '1', '2', '5', '10', '20', '50'])
    # ax_top.xaxis.set_minor_locator(ticker.LogLocator(base=10.0, numticks=5))
    ax_top.tick_params(direction='out', length=10, width=2, colors='black', pad=5,
                       top=False, bottom=True, labeltop=False, labelbottom=True,
                       labelsize=24)

    for tick in ax_top.get_xticklabels():
        # tick.set_fontname('Comic Sans MS')
        tick.set_fontname('American Typewriter')

    # Available Fonts
    # ['STIXSizeFourSym', 'DejaVu Sans Display', 'STIXNonUnicode', 'cmss10', 'STIXNonUnicode', 'DejaVu Sans Mono',
    #  'DejaVu Sans Mono', 'DejaVu Sans', 'DejaVu Serif Display', 'STIXSizeTwoSym', 'STIXSizeTwoSym', 'STIXGeneral',
    #  'STIXGeneral', 'STIXGeneral', 'cmmi10', 'STIXSizeOneSym', 'cmr10', 'DejaVu Sans', 'cmtt10', 'DejaVu Sans',
    #  'DejaVu Serif', 'STIXSizeThreeSym', 'STIXSizeOneSym', 'STIXSizeFourSym', 'STIXNonUnicode', 'cmex10', 'cmb10',
    #  'STIXSizeFiveSym', 'DejaVu Sans', 'DejaVu Sans Mono', 'STIXNonUnicode', 'STIXSizeThreeSym', 'DejaVu Sans Mono',
    #  'cmsy10', 'DejaVu Serif', 'DejaVu Serif', 'DejaVu Serif', 'STIXGeneral', 'Apple SD Gothic Neo', 'Zapf Dingbats',
    #  'Noto Nastaliq Urdu', 'Diwan Thuluth', 'Athelas', 'AppleGothic', 'Noto Sans Cypriot', 'Georgia', 'Galvji',
    #  'Myanmar MN', 'Charter', 'STIXNonUnicode', 'Hiragino Sans', 'STIXIntegralsUpD', 'Verdana', 'Kohinoor Gujarati',
    #  'DecoType Naskh', 'Plantagenet Cherokee', 'Noto Sans Cham', 'DIN Alternate', 'Hoefler Text', 'Comic Sans MS',
    #  'Noto Sans Sharada', 'Noto Sans Tifinagh', 'Cochin', 'STIXGeneral', 'Hiragino Sans', 'Noto Sans Old North Arabian',
    #  'Noto Sans Lydian', 'Noto Sans Siddham', 'Noto Sans Palmyrene', 'STIXSizeFiveSym', 'Noto Sans Linear A',
    #  'Noto Sans Tai Le', 'Mshtakan', 'Noto Sans Old Italic', 'Noto Sans PhagsPa', 'Arial Unicode MS', 'Courier New',
    #  'American Typewriter', 'Noto Sans Ol Chiki', 'ITF Devanagari', 'Snell Roundhand', 'Apple Braille', 'Al Bayan',
    #  'Arial Black', 'Songti SC', 'Georgia', 'Noto Sans Yi', 'Chalkduster', 'Noto Serif Yezidi', 'Noto Sans Hatran',
    #  'Arial', 'Noto Sans Khudawadi', 'Apple Braille', 'Bradley Hand', 'Hiragino Sans', 'Optima', 'Phosphate', 'Avenir',
    #  'Kohinoor Bangla', 'Savoye LET', 'InaiMathi', 'Times New Roman', 'Noto Sans Javanese', 'Impact',
    #  'Kannada Sangam MN', 'Marker Felt', 'STIXSizeTwoSym', 'Webdings', 'Oriya Sangam MN', 'PT Sans', 'STIXSizeFourSym',
    #  'Geeza Pro', 'Tamil MN', 'Gurmukhi MN', 'Georgia', 'Avenir Next Condensed', 'Noto Sans Limbu', 'STIXIntegralsUp',
    #  'Luminari', 'Verdana', '.SF NS Mono', 'Noto Sans Duployan', 'Arial Narrow', 'Arial Narrow', 'Academy Engraved LET',
    #  'New Peninim MT', 'Arial Narrow', 'Noto Sans Wancho', 'Tamil Sangam MN', 'Noto Sans Masaram Gondi',
    #  'Noto Sans Marchen', 'Kohinoor Devanagari', 'Noteworthy', 'Verdana', 'Noto Sans Brahmi', 'Apple Braille',
    #  'Noto Sans Buhid', 'Gurmukhi Sangam MN', 'Malayalam Sangam MN', 'Brush Script MT', 'Helvetica', 'PT Serif',
    #  'Big Caslon', 'Noto Sans Gunjala Gondi', 'Bodoni Ornaments', 'Trebuchet MS', 'Bangla MN', 'Herculanum',
    #  'Hiragino Maru Gothic Pro', 'AppleMyungjo', 'Comic Sans MS', 'Noto Sans NKo', 'Noto Sans Bhaiksuki',
    #  'Noto Sans Meetei Mayek', 'Al Tarikh', 'Times New Roman', 'Noto Sans Avestan', 'Baghdad', 'Noto Sans Syriac',
    #  'Krungthep', 'Monaco', 'STIXSizeOneSym', 'System Font', 'Noto Sans Multani', 'Noto Serif Myanmar',
    #  'Noto Sans Bassa Vah', '.SF Compact', 'Baskerville', 'Euphemia UCAS', 'Hiragino Sans', 'Marion', 'STIXSizeFourSym',
    #  'Noto Sans Modi', 'Noto Sans Mende Kikakui', 'Noto Sans Glagolitic', 'Bodoni 72 Smallcaps', 'Heiti TC', 'Geneva',
    #  'Noto Sans Tai Tham', 'Noto Sans Mongolian', 'Noto Sans Tai Viet', 'Nadeem', 'Seravek', 'Times New Roman',
    #  '.SF Compact Rounded', 'Corsiva Hebrew', 'Noto Sans Bamum', 'Farah', 'Noto Sans Rejang', 'Menlo',
    #  'Noto Sans Buginese', 'Hiragino Sans', 'Noto Sans Old Hungarian', 'Noto Sans Cuneiform', 'Andale Mono', 'Khmer MN',
    #  'Noto Sans Carian', 'Courier', 'Avenir Next', 'KufiStandardGK', 'Noto Sans Adlam', 'Kailasa',
    #  'Noto Sans Kharoshthi', 'STIXGeneral', 'Courier New', 'Farisi', 'Helvetica Neue', '.Keyboard',
    #  'Noto Serif Balinese', 'Noto Sans Caucasian Albanian', 'Trattatello', 'Sathu', 'Noto Sans Tagalog',
    #  'Noto Sans Osmanya', 'Noto Sans Miao', 'Noto Sans Phoenician', 'Devanagari Sangam MN', 'Hiragino Mincho ProN',
    #  'Noto Sans Hanifi Rohingya', 'Bodoni 72 Oldstyle', 'STIXVariants', 'Diwan Kufi', 'Noto Sans Egyptian Hieroglyphs',
    #  'Rockwell', 'Noto Sans Lycian', 'Futura', 'Noto Sans Pau Cin Hau', 'Noto Sans Ugaritic', 'STIXSizeOneSym',
    #  '.New York', 'STIXGeneral', 'Noto Sans Manichaean', 'STIXSizeTwoSym', 'Lao MN', 'Noto Sans Mro', 'Devanagari MT',
    #  'Wingdings 3', 'STIXGeneral', 'Noto Sans Meroitic', 'Gujarati Sangam MN', 'Apple Symbols', 'Noto Sans Warang Citi',
    #  'Wingdings 2', 'Didot', 'STIXIntegralsSm', 'Hiragino Sans', '.New York', 'Myanmar Sangam MN', 'Zapfino',
    #  'STIXNonUnicode', 'Shree Devanagari 714', 'Copperplate', 'Noto Sans Newa', 'Verdana', 'Noto Sans Thaana',
    #  'STIXIntegralsUpSm', 'Arial', 'Gujarati MT', 'STIXIntegralsD', 'Noto Sans Osage', 'Arial Rounded MT Bold', 'Arial',
    #  'Hiragino Sans', 'Wingdings', 'Malayalam MN', 'Arial Unicode MS', 'Courier New', 'DIN Condensed',
    #  'Noto Serif Ahom', 'System Font', 'Noto Sans Pahawh Hmong', 'Hiragino Sans GB', 'Heiti TC', 'Apple Braille',
    #  'Noto Sans Batak', 'Ayuthaya', 'Noto Sans Mandaic', 'Tahoma', 'Noto Sans Kayah Li', 'Noto Sans Linear B',
    #  'Bodoni 72', 'Lucida Grande', 'Noto Sans Coptic', '.SF NS Mono', 'Iowan Old Style', 'Hoefler Text', 'Courier New',
    #  'Hiragino Sans', 'Hiragino Sans', 'Kannada MN', 'Sana', 'Khmer Sangam MN', 'Tahoma', 'Noto Sans Tirhuta',
    #  'Thonburi', 'Chalkboard SE', 'Noto Sans Armenian', 'STIXNonUnicode', 'Gill Sans', 'Hiragino Sans', 'Apple Braille',
    #  'Silom', 'Palatino', 'Noto Sans Imperial Aramaic', 'Waseem', 'Kokonor', '.SF Arabic', 'Gurmukhi MT',
    #  'Noto Sans Khojki', 'Oriya MN', 'Noto Sans Elbasan', 'Mishafi', 'Noto Sans Syloti Nagri', 'Noto Sans Chakma',
    #  'Noto Sans Lisu', 'Noto Sans Old Persian', 'Kohinoor Telugu', 'Trebuchet MS', 'Georgia', 'STIXNonUnicode',
    #  'Noto Sans Old South Arabian', 'Noto Sans Nabataean', 'Noto Sans Vai', 'Chalkboard', 'Sinhala MN', 'PT Mono',
    #  'Mukta Mahee', 'Sinhala Sangam MN', 'STIXSizeThreeSym', '.SF NS Rounded', 'Beirut', 'Noto Sans Gothic',
    #  'Trebuchet MS', 'Noto Sans Kaithi', 'Superclarendon', 'Telugu Sangam MN', 'Lao Sangam MN', 'STIXIntegralsD',
    #  'Noto Sans Samaritan', 'Kefa', 'Noto Sans Old Turkic', 'Noto Sans Oriya', 'STIXSizeThreeSym', 'Apple Chancery',
    #  'Noto Sans Inscriptional Parthian', 'STIXIntegralsUpD', 'Noto Sans Myanmar', 'Raanana', 'PingFang HK', 'Skia',
    #  'Al Nile', 'Arial Hebrew', 'Telugu MN', 'Noto Sans Sundanese', 'Noto Sans Hanunoo', 'Noto Sans Lepcha',
    #  'Sukhumvit Set', 'STIXIntegralsSm', 'SignPainter', '.Aqua Kana', 'Noto Sans Tagbanwa', 'Noto Sans Old Permic',
    #  'Muna', 'STIXIntegralsUpSm', 'Noto Sans Sora Sompeng', 'Times New Roman', 'Mishafi Gold', 'Noto Sans Kannada',
    #  'Times', 'Party LET', 'Bangla Sangam MN', 'Damascus', 'PT Serif Caption', 'STIXIntegralsUp',
    #  'Microsoft Sans Serif', 'Symbol', 'Noto Sans Psalter Pahlavi', 'Arial Narrow', '.SF Compact',
    #  'Noto Sans Inscriptional Pahlavi', 'Arial', 'Trebuchet MS', 'Noto Sans New Tai Lue', 'STIXVariants',
    #  'Noto Sans Saurashtra', 'Papyrus', 'Noto Sans Mahajani', 'Noto Sans Takri']
    #
    # Add object names as annotations below the ticks
    # for obj, dist in object_distances.items():
    #     if log_min <= np.log10(dist) <= log_max:
    #         ax.annotate(obj, (dist, -0.25), ha='center', va='top', fontsize=8, rotation=45)
    jupiter_diameter = 1.42984e5
    giant_planet_reduction = 8
    small_planet_reduction = 3
    for obj, dist in object_distances.items():
        if obj in object_diameters:
            diameter = object_diameters[obj]
            if log_min <= np.log10(dist) <= log_max:
                # Calculate the radius without logarithmic scaling
                if diameter < 0.1*jupiter_diameter:
                    radius = diameter / (small_planet_reduction*jupiter_diameter)
                else:
                    radius = diameter / (giant_planet_reduction*jupiter_diameter)   # Adjust size to fit the visualization

                # print(radius)
                ax.add_patch(plt.Circle((np.log10(dist), 0.0), radius, color='black', alpha=0.9))
                # ax.annotate(obj, (dist, -0.25), ha='center', va='top', fontsize=8, rotation=45)

    ax.set_aspect('equal', 'box')
    ax.set_frame_on(False)
    plt.show()


if __name__ == '__main__':
    import matplotlib
    # matplotlib.use('module://backend_interagg')
    matplotlib.use('macosx')
    planetary_distances = read_json_file("semimajor_axes.json")
    planetary_diameters = read_json_file("diameters.json")
    draw_logarithmic_ruler(planetary_distances, planetary_diameters)
