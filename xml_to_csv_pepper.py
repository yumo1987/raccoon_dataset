import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    #image_path = os.path.join(os.getcwd(), 'Labels')
    image_path = r'D:\0.Works\External-Training\2-AIA\Course\0.FinalProject\Dataset\FBTUG\3-Data1+2\data3-1+2TwoTeamMerge-ByYM\labels_resize'
    xml_df = xml_to_csv(image_path)

    outputCSV = r'outputCSV\pepper_labels.csv'
    xml_df.to_csv(outputCSV, index=None)
    print('Successfully converted xml to csv.')


main()
