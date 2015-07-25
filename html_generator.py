# Stacy Bird (July 16, 2015)
# Stage 2 Submission File #3: html_generator.py
# The following code makes use of exercises found in Stage 2 class work

#The code below organizes the information contained in make_HTML
def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<h2 class="Title1">
    ''' + concept_title
    html_text_2 = '''
</h2>
    <div class="TextFormat Text1">
        <p>
        ''' + concept_description[0] + '''
        </p>
        <p>
        ''' + concept_description[1] + '''
        </p>
        <p>
        ''' + concept_description[2] + '''
        </p>
        <p>
        ''' + concept_description[2]
    html_text_3 = '''
        </p>
    </div>'''

    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

# This code will unpack the items contained in LIST_OF_CONCEPTS.
def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

# This is an example of what a list of concepts might look like.
LIST_OF_CONCEPTS = [ ['Break down the problem into its smallest possible components', ['''Start by writing 
        your ideas as pseudocode, putting into words the steps that 
        will eventually become code. Planning on paper before trying to work out the 
        correct code can save enormous amounts of time. ''',
        '''Once you have a good idea of what steps you need to take, write small bits 
        of code, test them and know what they do. ''',
        'Test, test, test!']],
                     ['Test, test, test!', ['There are several options for testing code as you write: ',
        'Add print statements, so that you can see the code at important points. ',
        'Use the assert function to test cases. ',
        'Write code that first tests only the simplest cases. ',
        'Add complexity and continue to test, test, test!']],
                             ["Don't Panic!", ['Seriously. ',
                              
        'Programming can be mind-explodingly difficult. ',
         '''If something is going wrong, step away/ take a break/ go to bed/
        get some fresh air/ try some exercise/ eat something delicious/ 
        read or watch something funny.''' ,
        "Don't.  Ever.  Panic."]]]

# This code will grab whatever is contained in LIST_OF_CONCEPTS
# and run it through make_HTML to be unpacked
def make_HTML_for_many_concepts(list_of_concepts):
    htmlText = """
                """
    for item in list_of_concepts:
        htmlText =  htmlText + make_HTML(item)
    return htmlText
        
    
print make_HTML_for_many_concepts(LIST_OF_CONCEPTS)


