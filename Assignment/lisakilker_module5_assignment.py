#Imports the class file library
import xml.etree.ElementTree as ET

#Program extrats the data from an XML file
def main():
    file_name = "cd_catalog.xml"
    #Parses through the XML file
    tree = ET.parse(file_name)
    #Gets the root element of the XML tree
    root = tree.getroot()

    #Extracts the data
    for cd_data in root.findall("CD"):

        #Checks for "Artist" and if it does not exist in the file it will display it as "Unknown"
        artist_element = cd_data.find("ARTIST")
        if artist_element is not None:
            artist = artist_element.text
        else:
            artist = "Unknown"

        #Checks for "Title" and if it does not exist in the file it will display it as "Unknown"
        title = cd_data.find("TITLE").text
        title_element = cd_data.find("TITLE")
        if title_element is not None:
            title = title_element.text
        else:
            title = "Unknown"
        
        #Checks for "Decade" and if it does not exist in the file it will display it as "Unknown"
        decade_element = cd_data.find("DECADE")
        if decade_element is not None:
            decade = decade_element.text
        else:
            decade = "Unknown"
        
        #Displays the data in a special format
        print(f"Artist: {artist}, Title: {title}, Decade: {decade}")

#Calls the main function
if __name__ == "__main__":
    main()