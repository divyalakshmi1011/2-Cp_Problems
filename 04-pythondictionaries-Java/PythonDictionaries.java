// Time to play with Python dictionaries!
// You're going to work on a dictionary that
// stores cities by country and continent.
// One is done for you - the city of Mountain 
// View is in the USA, which is in North America.

// You need to add the cities listed below by
// modifying the structure.
// Then, you should print out the values specified
// by looking them up in the structure.

// Cities to add:
// Bangalore (India, Asia)
// Atlanta (USA, North America)
// Cairo (Egypt, Africa)
// Shanghai (China, Asia)

// Print the following (using "print").
// 1. A list of all cities in the USA in
// alphabetic order. Create a non static method as alphaUSA() which returns list
// 2. All cities in Asia, in alphabetic
// order, next to the name of the country.
// In your output, label each answer with a number, Create a non static 
// method alphaAsia() which returns list, so it looks like this:
// 1
// American City
// American City
// 2
// Asian City - Country
// Asian City - Country
// locations = {'North America': {'USA': ['Mountain View']}}
import java.util.*;
public class PythonDictionaries {
    Map<String, Map<String,ArrayList<String>>> myMap;
	public PythonDictionaries() {
		Map<String, Map<String,ArrayList<String>>> myMap = new HashMap<String, Map<String,ArrayList<String>>>();
		Map<String,ArrayList<String>> m = new Map<String,ArrayList<String>>();
		ArrayList l = new ArrayList<String>();
		l.add("Atlanta");
		l.add("Mountain View");
        m.put("USA",l);
		myMap.put("North America", m);
	}
	public List<String> alphaUSA() {
		// Your code goes here
		
		return null;
	}

	public List<String> sortAsia() {
		// Your code goes here
		return null;
	}
	
}